from aiohh.methods.base import BaseMethod
from aiohh.types.common import Items
from aiohh.types.employer import VacancyBrandedTemplateItem


class GetVacancyBrandedTemplates(BaseMethod[Items[VacancyBrandedTemplateItem]]):
    __returning__ = Items[VacancyBrandedTemplateItem]
    __endpoint__ = "/employers/{employer_id}/vacancy_branded_templates"

    employer_id: int | str
