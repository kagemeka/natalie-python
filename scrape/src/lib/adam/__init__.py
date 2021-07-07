import typing
from .make_df import (
  MakeAdamDFs,
  AdamDF,
)
from .store import (
  StoreDF,
)



class Adam():
  def __call__(
    self,
  ) -> typing.NoReturn:
    self.__make_df()
    self.__store()
  

  def __make_df(
    self,
  ) -> typing.NoReturn:
    self.__df = MakeAdamDFs()()
  

  def __store(
    self,
  ) -> typing.NoReturn:
    StoreDF()(self.__df)