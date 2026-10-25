from pydantic import BaseModel, ConfigDict


class BaseType(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True, validate_by_name=True)
