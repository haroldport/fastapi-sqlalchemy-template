from functools import wraps
from typing import Any, Callable, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")

class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
            raise exc_val
        else:
            await self.session.commit()

class UnitOfWorkWrapper:
    def __init__(self, use_case: Any, session: AsyncSession):
        self._use_case = use_case
        self._session = session

        for attr_name in dir(use_case):
            if not attr_name.startswith("_"):
                attr = getattr(use_case, attr_name)
                if callable(attr):
                    if hasattr(attr, "__code__") and attr.__code__.co_flags & 0x80:
                        setattr(self, attr_name, self._wrap_with_uow(attr))
                    else:
                        setattr(self, attr_name, attr)
                else:
                    setattr(self, attr_name, attr)

    def _wrap_with_uow(self, method: Callable) -> Callable:
        @wraps(method)
        async def wrapper(*args, **kwargs):
            use_case_instance = self._use_case
            try:
                result = await method(*args, **kwargs)
                await self._session.commit()
                return result
            except Exception as e:
                await self._session.rollback()
                if hasattr(use_case_instance, "on_save_failure"):
                    await use_case_instance.on_save_failure()
                raise e
        return wrapper
