from datetime import date, datetime
from types import TracebackType
from typing import Any, Literal

from aiohh.client.session.aiohttp import AiohttpSession
from aiohh.client.session.base import BaseSession
from aiohh.enums.host import Host
from aiohh.methods.add_applicant_comment import AddApplicantComment
from aiohh.methods.add_chat_participant import AddChatParticipant
from aiohh.methods.add_employer_manager import AddEmployerManager
from aiohh.methods.archive_vacancy import ArchiveVacancy
from aiohh.methods.base import BaseMethod, ReturningType
from aiohh.methods.change_negotiation_state import ChangeNegotiationState
from aiohh.methods.create_chat_without_vacancy import CreateChatWithoutVacancy
from aiohh.methods.create_saved_resume_search import CreateSavedResumeSearch
from aiohh.methods.create_vacancy_draft import CreateVacancyDraft
from aiohh.methods.create_webhook_subscription import CreateWebhookSubscription
from aiohh.methods.delete_applicant_comment import DeleteApplicantComment
from aiohh.methods.delete_chat_message import DeleteChatMessage
from aiohh.methods.delete_employer_manager import DeleteEmployerManager
from aiohh.methods.delete_saved_resume_search import DeleteSavedResumeSearch
from aiohh.methods.delete_vacancy_draft import DeleteVacancyDraft
from aiohh.methods.delete_webhook_subscription import DeleteWebhookSubscription
from aiohh.methods.disable_draft_auto_publication import DisableDraftAutoPublication
from aiohh.methods.edit_chat_message import EditChatMessage
from aiohh.methods.edit_employer_manager import EditEmployerManager
from aiohh.methods.edit_vacancy import EditVacancy
from aiohh.methods.edit_vacancy_draft import EditVacancyDraft
from aiohh.methods.get_active_vacancies import GetActiveVacancies
from aiohh.methods.get_applicant_comments import GetApplicantComments
from aiohh.methods.get_application_token import GetApplicationToken
from aiohh.methods.get_archived_vacancies import GetArchivedVacancies
from aiohh.methods.get_area import GetArea
from aiohh.methods.get_areas import GetAreas
from aiohh.methods.get_available_publications import GetAvailablePublications
from aiohh.methods.get_call_link import GetCallLink
from aiohh.methods.get_calls_history import GetCallsHistory
from aiohh.methods.get_chat_file_upload_link import GetChatFileUploadLink
from aiohh.methods.get_chat_files_conditions import GetChatFilesConditions
from aiohh.methods.get_chat_messages import GetChatMessages
from aiohh.methods.get_chat_participants import GetChatParticipants
from aiohh.methods.get_chats import GetChats
from aiohh.methods.get_city_metro import GetCityMetro
from aiohh.methods.get_clickme_statistics import GetClickmeStatistics
from aiohh.methods.get_collection_negotiations import GetCollectionNegotiations
from aiohh.methods.get_countries import GetCountries
from aiohh.methods.get_dictionaries import GetDictionaries
from aiohh.methods.get_districts import GetDistricts
from aiohh.methods.get_educational_institutions import GetEducationalInstitutions
from aiohh.methods.get_employer import GetEmployer
from aiohh.methods.get_employer_address import GetEmployerAddress
from aiohh.methods.get_employer_addresses import GetEmployerAddresses
from aiohh.methods.get_employer_departments import GetEmployerDepartments
from aiohh.methods.get_employer_manager import GetEmployerManager
from aiohh.methods.get_employer_manager_types import GetEmployerManagerTypes
from aiohh.methods.get_employer_managers import GetEmployerManagers
from aiohh.methods.get_employer_negotiations_statistics import (
    GetEmployerNegotiationsStatistics,
)
from aiohh.methods.get_employer_services import GetEmployerServices
from aiohh.methods.get_employer_tests import GetEmployerTests
from aiohh.methods.get_employer_vacancy_areas import GetEmployerVacancyAreas
from aiohh.methods.get_faculties import GetFaculties
from aiohh.methods.get_hidden_vacancies import GetHiddenVacancies
from aiohh.methods.get_industries import GetIndustries
from aiohh.methods.get_languages import GetLanguages
from aiohh.methods.get_locales import GetLocales
from aiohh.methods.get_mail_templates import GetMailTemplates
from aiohh.methods.get_manager_accounts import GetManagerAccounts
from aiohh.methods.get_manager_negotiations_statistics import (
    GetManagerNegotiationsStatistics,
)
from aiohh.methods.get_manager_resume_limits import GetManagerResumeLimits
from aiohh.methods.get_manager_settings import GetManagerSettings
from aiohh.methods.get_me import GetMe
from aiohh.methods.get_message_templates import GetMessageTemplates
from aiohh.methods.get_method_access import GetMethodAccess
from aiohh.methods.get_metro import GetMetro
from aiohh.methods.get_negotiation import GetNegotiation
from aiohh.methods.get_negotiation_collections import GetNegotiationCollections
from aiohh.methods.get_negotiation_messages import GetNegotiationMessages
from aiohh.methods.get_negotiation_test_result import GetNegotiationTestResult
from aiohh.methods.get_preferred_negotiations_order import GetPreferredNegotiationsOrder
from aiohh.methods.get_professional_roles import GetProfessionalRoles
from aiohh.methods.get_related_vacancies import GetRelatedVacancies
from aiohh.methods.get_resume import GetResume
from aiohh.methods.get_resume_locales import GetResumeLocales
from aiohh.methods.get_resume_negotiations_history import GetResumeNegotiationsHistory
from aiohh.methods.get_salary_areas import GetSalaryAreas
from aiohh.methods.get_salary_employee_levels import GetSalaryEmployeeLevels
from aiohh.methods.get_salary_evaluation import GetSalaryEvaluation
from aiohh.methods.get_salary_industries import GetSalaryIndustries
from aiohh.methods.get_salary_professional_areas import GetSalaryProfessionalAreas
from aiohh.methods.get_saved_resume_search import GetSavedResumeSearch
from aiohh.methods.get_saved_resume_searches import GetSavedResumeSearches
from aiohh.methods.get_similar_vacancies import GetSimilarVacancies
from aiohh.methods.get_skills import GetSkills
from aiohh.methods.get_unread_chats_count import GetUnreadChatsCount
from aiohh.methods.get_user_token import GetUserToken
from aiohh.methods.get_vacancy import GetVacancy
from aiohh.methods.get_vacancy_branded_templates import GetVacancyBrandedTemplates
from aiohh.methods.get_vacancy_conditions import GetVacancyConditions
from aiohh.methods.get_vacancy_draft import GetVacancyDraft
from aiohh.methods.get_vacancy_draft_duplicates import GetVacancyDraftDuplicates
from aiohh.methods.get_vacancy_drafts import GetVacancyDrafts
from aiohh.methods.get_vacancy_prolongation import GetVacancyProlongation
from aiohh.methods.get_vacancy_stats import GetVacancyStats
from aiohh.methods.get_vacancy_upgrades import GetVacancyUpgrades
from aiohh.methods.get_vacancy_visitors import GetVacancyVisitors
from aiohh.methods.get_webhook_subscriptions import GetWebhookSubscriptions
from aiohh.methods.hide_vacancy import HideVacancy
from aiohh.methods.invalidate_token import InvalidateToken
from aiohh.methods.invite_applicant import InviteApplicant
from aiohh.methods.leave_chat import LeaveChat
from aiohh.methods.mark_chat_message_read import MarkChatMessageRead
from aiohh.methods.mark_negotiations_read import MarkNegotiationsRead
from aiohh.methods.move_negotiation import MoveNegotiation
from aiohh.methods.move_saved_resume_search import MoveSavedResumeSearch
from aiohh.methods.prolongate_vacancy import ProlongateVacancy
from aiohh.methods.publish_vacancy import PublishVacancy
from aiohh.methods.publish_vacancy_draft import PublishVacancyDraft
from aiohh.methods.refresh_user_token import RefreshUserToken
from aiohh.methods.restore_vacancy import RestoreVacancy
from aiohh.methods.search_call_transcripts import SearchCallTranscripts
from aiohh.methods.search_employers import SearchEmployers
from aiohh.methods.search_resumes import SearchResumes
from aiohh.methods.search_vacancies import SearchVacancies
from aiohh.methods.send_chat_message import SendChatMessage
from aiohh.methods.set_chat_write_possibility import SetChatWritePossibility
from aiohh.methods.set_preferred_negotiations_order import SetPreferredNegotiationsOrder
from aiohh.methods.suggest_area_leaves import SuggestAreaLeaves
from aiohh.methods.suggest_areas import SuggestAreas
from aiohh.methods.suggest_companies import SuggestCompanies
from aiohh.methods.suggest_educational_institutions import (
    SuggestEducationalInstitutions,
)
from aiohh.methods.suggest_fields_of_study import SuggestFieldsOfStudy
from aiohh.methods.suggest_positions import SuggestPositions
from aiohh.methods.suggest_professional_roles import SuggestProfessionalRoles
from aiohh.methods.suggest_resume_search_keywords import SuggestResumeSearchKeywords
from aiohh.methods.suggest_skills import SuggestSkills
from aiohh.methods.suggest_vacancy_positions import SuggestVacancyPositions
from aiohh.methods.suggest_vacancy_search_keywords import SuggestVacancySearchKeywords
from aiohh.methods.update_applicant_comment import UpdateApplicantComment
from aiohh.methods.update_mail_template import UpdateMailTemplate
from aiohh.methods.update_saved_resume_search import UpdateSavedResumeSearch
from aiohh.methods.update_webhook_subscription import UpdateWebhookSubscription
from aiohh.types.area import Area
from aiohh.types.call import CallLink, CallsHistory, CallTranscripts
from aiohh.types.chat import (
    Chat,
    ChatFilesConditions,
    ChatFileUploadLink,
    ChatMessages,
    ChatParticipant,
    UnreadChatsCount,
)
from aiohh.types.common import AreaLink, Id, IdName, Items, Page
from aiohh.types.dictionaries import (
    Dictionaries,
    District,
    EducationalInstitution,
    Industry,
    Language,
    Locale,
    ProfessionalRolesCatalog,
    Skill,
)
from aiohh.types.draft import (
    DraftResponse,
    PublishedDraft,
    VacancyDraft,
    VacancyDraftItem,
    VacancyDuplicates,
)
from aiohh.types.employer import (
    AvailablePublications,
    Employer,
    EmployerAddress,
    EmployerItem,
    EmployerService,
    MethodAccess,
    VacancyBrandedTemplateItem,
)
from aiohh.types.employer_vacancy import (
    EmployerVacancy,
    PreferredNegotiationsOrder,
    VacancyFieldCondition,
    VacancyProlongation,
    VacancyStatsItem,
    VacancyUpgrades,
)
from aiohh.types.manager import (
    EmployerManager,
    EmployerManagerItem,
    ManagerAccounts,
    ManagerPhone,
    ManagerResumeLimits,
    ManagerSettings,
    ManagerType,
)
from aiohh.types.me import Me
from aiohh.types.metro import MetroCity
from aiohh.types.negotiation import (
    ApplicantComment,
    EmployerNegotiationsStatistics,
    MailTemplate,
    ManagerNegotiationsStatistics,
    MessageTemplates,
    Negotiation,
    NegotiationMessage,
    NegotiationsCollections,
    NegotiationsPage,
    NegotiationTestResult,
)
from aiohh.types.resume import (
    NegotiationsHistory,
    Resume,
    ResumeSearchText,
    ResumesPage,
    SavedResumeSearch,
    VisitorsPage,
)
from aiohh.types.statistics import (
    ClickmeStatisticsItem,
    IdNameDescription,
    SalaryArea,
    SalaryEvaluation,
    SalaryProfessionalArea,
)
from aiohh.types.suggests import (
    AreaSuggest,
    CompanySuggest,
    FieldOfStudySuggest,
    KeywordSuggests,
    PositionSuggest,
    ProfessionalRoleSuggest,
    VacancyPositionSuggest,
)
from aiohh.types.token import ApplicationToken, UserToken
from aiohh.types.vacancy import (
    AutoResponse,
    Contacts,
    KeySkill,
    VacanciesPage,
    Vacancy,
    VacancyTest,
)
from aiohh.types.vacancy_input import (
    SalaryRangeInput,
    VacancyAddressInput,
    VacancyLanguageInput,
    VacancyPropertiesInput,
)
from aiohh.types.webhook import WebhookAction, WebhookSubscription

USER_AGENT_HEADER = "HH-User-Agent"
AUTHORIZATION_HEADER = "Authorization"
MANAGER_ACCOUNT_HEADER = "X-Manager-Account-Id"


class AiohhAPI:

    def __init__(
        self,
        *,
        user_agent: str,
        access_token: str | None = None,
        manager_account_id: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
        session: BaseSession | None = None,
    ) -> None:
        self.user_agent = user_agent
        self.access_token = access_token
        self.manager_account_id = manager_account_id
        self.host = host
        self.locale = locale
        self.session = session or AiohttpSession()

    async def __aenter__(self) -> "AiohhAPI":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def __call__(self, method: BaseMethod[ReturningType]) -> ReturningType:
        return await self.session(
            method=self.apply_defaults(method), headers=self.build_headers(method)
        )

    async def close(self) -> None:
        await self.session.close()

    def build_headers(self, method: BaseMethod[Any]) -> dict[str, str]:
        headers = {USER_AGENT_HEADER: self.user_agent}

        if not method.__authorized__:
            return headers

        if self.access_token is not None:
            headers[AUTHORIZATION_HEADER] = f"Bearer {self.access_token}"

        if self.manager_account_id is not None:
            headers[MANAGER_ACCOUNT_HEADER] = self.manager_account_id

        return headers

    def apply_defaults(
        self, method: BaseMethod[ReturningType]
    ) -> BaseMethod[ReturningType]:
        defaults = {
            name: value
            for name, value in (("host", self.host), ("locale", self.locale))
            if value is not None and getattr(method, name) is None
        }

        if not defaults:
            return method

        return method.model_copy(update=defaults)

    async def get_me(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Me:
        return await self(GetMe(host=host, locale=locale))

    async def search_vacancies(
        self,
        *,
        text: str | None = None,
        search_field: list[str] | None = None,
        experience: list[str] | None = None,
        employment_form: list[str] | None = None,
        work_format: list[str] | None = None,
        work_schedule_by_days: list[str] | None = None,
        working_hours: list[str] | None = None,
        area: list[int | str] | None = None,
        metro: list[int | str] | None = None,
        professional_role: list[int | str] | None = None,
        industry: list[int | str] | None = None,
        employer_id: list[int | str] | None = None,
        currency: str | None = None,
        salary: int | None = None,
        salary_frequency: list[str] | None = None,
        salary_mode: str | None = None,
        label: list[str] | None = None,
        education: list[str] | None = None,
        driver_license_types: list[str] | None = None,
        period: int | None = None,
        date_from: date | datetime | None = None,
        date_to: date | datetime | None = None,
        top_lat: float | None = None,
        bottom_lat: float | None = None,
        left_lng: float | None = None,
        right_lng: float | None = None,
        order_by: str | None = None,
        sort_point_lat: float | None = None,
        sort_point_lng: float | None = None,
        clusters: bool | None = None,
        describe_arguments: bool | None = None,
        no_magic: bool | None = None,
        responses_count_enabled: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        accept_temporary: bool | None = None,
        excluded_text: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacanciesPage:
        return await self(
            SearchVacancies(
                host=host,
                locale=locale,
                text=text,
                search_field=search_field,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                area=area,
                metro=metro,
                professional_role=professional_role,
                industry=industry,
                employer_id=employer_id,
                currency=currency,
                salary=salary,
                salary_frequency=salary_frequency,
                salary_mode=salary_mode,
                label=label,
                education=education,
                driver_license_types=driver_license_types,
                period=period,
                date_from=date_from,
                date_to=date_to,
                top_lat=top_lat,
                bottom_lat=bottom_lat,
                left_lng=left_lng,
                right_lng=right_lng,
                order_by=order_by,
                sort_point_lat=sort_point_lat,
                sort_point_lng=sort_point_lng,
                clusters=clusters,
                describe_arguments=describe_arguments,
                no_magic=no_magic,
                responses_count_enabled=responses_count_enabled,
                page=page,
                per_page=per_page,
                accept_temporary=accept_temporary,
                excluded_text=excluded_text,
            )
        )

    async def get_vacancy(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Vacancy:
        return await self(GetVacancy(host=host, locale=locale, vacancy_id=vacancy_id))

    async def get_similar_vacancies(
        self,
        vacancy_id: int | str,
        *,
        text: str | None = None,
        search_field: list[str] | None = None,
        experience: list[str] | None = None,
        employment_form: list[str] | None = None,
        work_format: list[str] | None = None,
        work_schedule_by_days: list[str] | None = None,
        working_hours: list[str] | None = None,
        area: list[int | str] | None = None,
        metro: list[int | str] | None = None,
        professional_role: list[int | str] | None = None,
        industry: list[int | str] | None = None,
        employer_id: list[int | str] | None = None,
        currency: str | None = None,
        salary: int | None = None,
        salary_frequency: list[str] | None = None,
        salary_mode: str | None = None,
        label: list[str] | None = None,
        education: list[str] | None = None,
        driver_license_types: list[str] | None = None,
        period: int | None = None,
        date_from: date | datetime | None = None,
        date_to: date | datetime | None = None,
        top_lat: float | None = None,
        bottom_lat: float | None = None,
        left_lng: float | None = None,
        right_lng: float | None = None,
        order_by: str | None = None,
        sort_point_lat: float | None = None,
        sort_point_lng: float | None = None,
        clusters: bool | None = None,
        describe_arguments: bool | None = None,
        no_magic: bool | None = None,
        responses_count_enabled: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        excluded_employer_id: list[int | str] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacanciesPage:
        return await self(
            GetSimilarVacancies(
                host=host,
                locale=locale,
                text=text,
                search_field=search_field,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                area=area,
                metro=metro,
                professional_role=professional_role,
                industry=industry,
                employer_id=employer_id,
                currency=currency,
                salary=salary,
                salary_frequency=salary_frequency,
                salary_mode=salary_mode,
                label=label,
                education=education,
                driver_license_types=driver_license_types,
                period=period,
                date_from=date_from,
                date_to=date_to,
                top_lat=top_lat,
                bottom_lat=bottom_lat,
                left_lng=left_lng,
                right_lng=right_lng,
                order_by=order_by,
                sort_point_lat=sort_point_lat,
                sort_point_lng=sort_point_lng,
                clusters=clusters,
                describe_arguments=describe_arguments,
                no_magic=no_magic,
                responses_count_enabled=responses_count_enabled,
                page=page,
                per_page=per_page,
                vacancy_id=vacancy_id,
                excluded_employer_id=excluded_employer_id,
            )
        )

    async def get_related_vacancies(
        self,
        vacancy_id: int | str,
        *,
        text: str | None = None,
        search_field: list[str] | None = None,
        experience: list[str] | None = None,
        employment_form: list[str] | None = None,
        work_format: list[str] | None = None,
        work_schedule_by_days: list[str] | None = None,
        working_hours: list[str] | None = None,
        area: list[int | str] | None = None,
        metro: list[int | str] | None = None,
        professional_role: list[int | str] | None = None,
        industry: list[int | str] | None = None,
        employer_id: list[int | str] | None = None,
        currency: str | None = None,
        salary: int | None = None,
        salary_frequency: list[str] | None = None,
        salary_mode: str | None = None,
        label: list[str] | None = None,
        education: list[str] | None = None,
        driver_license_types: list[str] | None = None,
        period: int | None = None,
        date_from: date | datetime | None = None,
        date_to: date | datetime | None = None,
        top_lat: float | None = None,
        bottom_lat: float | None = None,
        left_lng: float | None = None,
        right_lng: float | None = None,
        order_by: str | None = None,
        sort_point_lat: float | None = None,
        sort_point_lng: float | None = None,
        clusters: bool | None = None,
        describe_arguments: bool | None = None,
        no_magic: bool | None = None,
        responses_count_enabled: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        excluded_employer_id: list[int | str] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacanciesPage:
        return await self(
            GetRelatedVacancies(
                host=host,
                locale=locale,
                text=text,
                search_field=search_field,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                area=area,
                metro=metro,
                professional_role=professional_role,
                industry=industry,
                employer_id=employer_id,
                currency=currency,
                salary=salary,
                salary_frequency=salary_frequency,
                salary_mode=salary_mode,
                label=label,
                education=education,
                driver_license_types=driver_license_types,
                period=period,
                date_from=date_from,
                date_to=date_to,
                top_lat=top_lat,
                bottom_lat=bottom_lat,
                left_lng=left_lng,
                right_lng=right_lng,
                order_by=order_by,
                sort_point_lat=sort_point_lat,
                sort_point_lng=sort_point_lng,
                clusters=clusters,
                describe_arguments=describe_arguments,
                no_magic=no_magic,
                responses_count_enabled=responses_count_enabled,
                page=page,
                per_page=per_page,
                vacancy_id=vacancy_id,
                excluded_employer_id=excluded_employer_id,
            )
        )

    async def search_employers(
        self,
        *,
        text: str | None = None,
        area: list[int | str] | None = None,
        type: list[str] | None = None,
        only_with_vacancies: bool | None = None,
        sort_by: Literal["by_name", "by_vacancies_open"] | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerItem]:
        return await self(
            SearchEmployers(
                host=host,
                locale=locale,
                text=text,
                area=area,
                type=type,
                only_with_vacancies=only_with_vacancies,
                sort_by=sort_by,
                page=page,
                per_page=per_page,
            )
        )

    async def get_employer(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Employer:
        return await self(
            GetEmployer(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_dictionaries(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Dictionaries:
        return await self(GetDictionaries(host=host, locale=locale))

    async def get_industries(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Industry]:
        return await self(GetIndustries(host=host, locale=locale))

    async def get_professional_roles(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ProfessionalRolesCatalog:
        return await self(GetProfessionalRoles(host=host, locale=locale))

    async def get_languages(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Language]:
        return await self(GetLanguages(host=host, locale=locale))

    async def get_locales(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Locale]:
        return await self(GetLocales(host=host, locale=locale))

    async def get_resume_locales(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Locale]:
        return await self(GetResumeLocales(host=host, locale=locale))

    async def get_skills(
        self,
        id: list[int | str],
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[Skill]:
        return await self(GetSkills(host=host, locale=locale, id=id))

    async def get_educational_institutions(
        self,
        id: list[int | str],
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[EducationalInstitution]:
        return await self(GetEducationalInstitutions(host=host, locale=locale, id=id))

    async def get_faculties(
        self,
        educational_institution_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[IdName]:
        return await self(
            GetFaculties(
                host=host,
                locale=locale,
                educational_institution_id=educational_institution_id,
            )
        )

    async def get_districts(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[District]:
        return await self(GetDistricts(host=host, locale=locale))

    async def get_metro(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[MetroCity]:
        return await self(GetMetro(host=host, locale=locale))

    async def get_city_metro(
        self,
        city_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> MetroCity:
        return await self(GetCityMetro(host=host, locale=locale, city_id=city_id))

    async def get_areas(
        self,
        *,
        additional_case: Literal["prepositional"] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Area]:
        return await self(
            GetAreas(host=host, locale=locale, additional_case=additional_case)
        )

    async def get_area(
        self,
        area_id: int | str,
        *,
        additional_case: Literal["prepositional"] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Area:
        return await self(
            GetArea(
                host=host,
                locale=locale,
                area_id=area_id,
                additional_case=additional_case,
            )
        )

    async def get_countries(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[AreaLink]:
        return await self(GetCountries(host=host, locale=locale))

    async def suggest_positions(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[PositionSuggest]:
        return await self(SuggestPositions(host=host, locale=locale, text=text))

    async def suggest_vacancy_positions(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[VacancyPositionSuggest]:
        return await self(SuggestVacancyPositions(host=host, locale=locale, text=text))

    async def suggest_areas(
        self,
        text: str,
        *,
        area_id: int | str | None = None,
        include_parent: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[AreaSuggest]:
        return await self(
            SuggestAreas(
                host=host,
                locale=locale,
                text=text,
                area_id=area_id,
                include_parent=include_parent,
            )
        )

    async def suggest_area_leaves(
        self,
        text: str,
        *,
        area_id: int | str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[AreaSuggest]:
        return await self(
            SuggestAreaLeaves(host=host, locale=locale, text=text, area_id=area_id)
        )

    async def suggest_fields_of_study(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[FieldOfStudySuggest]:
        return await self(SuggestFieldsOfStudy(host=host, locale=locale, text=text))

    async def suggest_professional_roles(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[ProfessionalRoleSuggest]:
        return await self(SuggestProfessionalRoles(host=host, locale=locale, text=text))

    async def suggest_companies(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[CompanySuggest]:
        return await self(SuggestCompanies(host=host, locale=locale, text=text))

    async def suggest_educational_institutions(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[EducationalInstitution]:
        return await self(
            SuggestEducationalInstitutions(host=host, locale=locale, text=text)
        )

    async def suggest_skills(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[Skill]:
        return await self(SuggestSkills(host=host, locale=locale, text=text))

    async def suggest_vacancy_search_keywords(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> KeywordSuggests:
        return await self(
            SuggestVacancySearchKeywords(host=host, locale=locale, text=text)
        )

    async def suggest_resume_search_keywords(
        self,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> KeywordSuggests:
        return await self(
            SuggestResumeSearchKeywords(host=host, locale=locale, text=text)
        )

    async def get_user_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        *,
        redirect_uri: str | None = None,
        code_verifier: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> UserToken:
        return await self(
            GetUserToken(
                host=host,
                locale=locale,
                client_id=client_id,
                client_secret=client_secret,
                code=code,
                redirect_uri=redirect_uri,
                code_verifier=code_verifier,
            )
        )

    async def refresh_user_token(
        self,
        refresh_token: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> UserToken:
        return await self(
            RefreshUserToken(host=host, locale=locale, refresh_token=refresh_token)
        )

    async def get_application_token(
        self,
        client_id: str,
        client_secret: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ApplicationToken:
        return await self(
            GetApplicationToken(
                host=host,
                locale=locale,
                client_id=client_id,
                client_secret=client_secret,
            )
        )

    async def invalidate_token(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(InvalidateToken(host=host, locale=locale))

    async def get_manager_accounts(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ManagerAccounts:
        return await self(GetManagerAccounts(host=host, locale=locale))

    async def get_employer_managers(
        self,
        employer_id: int | str,
        *,
        search_text: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerManagerItem]:
        return await self(
            GetEmployerManagers(
                host=host,
                locale=locale,
                employer_id=employer_id,
                search_text=search_text,
                page=page,
                per_page=per_page,
            )
        )

    async def add_employer_manager(
        self,
        employer_id: int | str,
        email: str,
        first_name: str,
        last_name: str,
        position: str,
        area: Id,
        phone: ManagerPhone,
        is_main_contact_person: bool,
        *,
        middle_name: str | None = None,
        additional_phone: ManagerPhone | None = None,
        permissions: list[Id] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Id:
        return await self(
            AddEmployerManager(
                host=host,
                locale=locale,
                employer_id=employer_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                position=position,
                area=area,
                phone=phone,
                additional_phone=additional_phone,
                is_main_contact_person=is_main_contact_person,
                permissions=permissions,
            )
        )

    async def get_employer_manager(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> EmployerManager:
        return await self(
            GetEmployerManager(
                host=host, locale=locale, employer_id=employer_id, manager_id=manager_id
            )
        )

    async def edit_employer_manager(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        position: str | None = None,
        phone: ManagerPhone | None = None,
        additional_phone: ManagerPhone | None = None,
        permissions: list[Id] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            EditEmployerManager(
                host=host,
                locale=locale,
                employer_id=employer_id,
                manager_id=manager_id,
                position=position,
                phone=phone,
                additional_phone=additional_phone,
                permissions=permissions,
            )
        )

    async def delete_employer_manager(
        self,
        employer_id: int | str,
        manager_id: int | str,
        successor_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteEmployerManager(
                host=host,
                locale=locale,
                employer_id=employer_id,
                manager_id=manager_id,
                successor_id=successor_id,
            )
        )

    async def get_employer_manager_types(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[ManagerType]:
        return await self(
            GetEmployerManagerTypes(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_manager_resume_limits(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ManagerResumeLimits:
        return await self(
            GetManagerResumeLimits(
                host=host, locale=locale, employer_id=employer_id, manager_id=manager_id
            )
        )

    async def get_manager_settings(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ManagerSettings:
        return await self(
            GetManagerSettings(
                host=host, locale=locale, employer_id=employer_id, manager_id=manager_id
            )
        )

    async def get_employer_addresses(
        self,
        employer_id: int | str,
        *,
        changed_after: datetime | None = None,
        manager_id: int | str | None = None,
        with_manager: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerAddress]:
        return await self(
            GetEmployerAddresses(
                host=host,
                locale=locale,
                employer_id=employer_id,
                changed_after=changed_after,
                manager_id=manager_id,
                with_manager=with_manager,
                page=page,
                per_page=per_page,
            )
        )

    async def get_employer_address(
        self,
        employer_id: int | str,
        address_id: int | str,
        *,
        with_manager: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> EmployerAddress:
        return await self(
            GetEmployerAddress(
                host=host,
                locale=locale,
                employer_id=employer_id,
                address_id=address_id,
                with_manager=with_manager,
            )
        )

    async def get_employer_departments(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[IdName]:
        return await self(
            GetEmployerDepartments(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_vacancy_branded_templates(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[VacancyBrandedTemplateItem]:
        return await self(
            GetVacancyBrandedTemplates(
                host=host, locale=locale, employer_id=employer_id
            )
        )

    async def get_employer_vacancy_areas(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[AreaLink]:
        return await self(
            GetEmployerVacancyAreas(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_employer_tests(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[IdName]:
        return await self(
            GetEmployerTests(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_employer_services(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[EmployerService]:
        return await self(
            GetEmployerServices(host=host, locale=locale, employer_id=employer_id)
        )

    async def get_method_access(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[MethodAccess]:
        return await self(
            GetMethodAccess(
                host=host, locale=locale, employer_id=employer_id, manager_id=manager_id
            )
        )

    async def get_available_publications(
        self,
        employer_id: int | str,
        *,
        area_id: int | str | None = None,
        professional_role_id: int | str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> AvailablePublications:
        return await self(
            GetAvailablePublications(
                host=host,
                locale=locale,
                employer_id=employer_id,
                area_id=area_id,
                professional_role_id=professional_role_id,
            )
        )

    async def search_resumes(
        self,
        *,
        text: list[ResumeSearchText] | None = None,
        area: list[int | str] | None = None,
        metro: list[int | str] | None = None,
        relocation: str | None = None,
        period: int | None = None,
        date_from: date | datetime | None = None,
        date_to: date | datetime | None = None,
        age_from: int | None = None,
        age_to: int | None = None,
        gender: str | None = None,
        experience: list[str] | None = None,
        skill: list[int | str] | None = None,
        language: list[str] | None = None,
        label: list[str] | None = None,
        currency: str | None = None,
        salary_from: int | None = None,
        salary_to: int | None = None,
        professional_role: list[int | str] | None = None,
        citizenship: list[int | str] | None = None,
        work_ticket: list[int | str] | None = None,
        educational_institution: list[int | str] | None = None,
        driver_license_types: list[str] | None = None,
        search_in_responses: bool | None = None,
        by_text_prefix: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        employment_form: list[str] | None = None,
        work_format: list[str] | None = None,
        education_levels: list[str] | None = None,
        job_search_status: list[str] | None = None,
        business_trip_readiness: list[str] | None = None,
        district: list[int | str] | None = None,
        filter_exp_industry: str | None = None,
        filter_exp_period: str | None = None,
        vacancy_id: int | str | None = None,
        resume: str | None = None,
        folder: list[int | str] | None = None,
        include_all_folders: bool | None = None,
        with_job_search_status: bool | None = None,
        saved_search_id: int | str | None = None,
        search_by_vacancy_id: int | str | None = None,
        last_used: datetime | None = None,
        last_used_timestamp: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ResumesPage:
        return await self(
            SearchResumes(
                host=host,
                locale=locale,
                text=text,
                area=area,
                metro=metro,
                relocation=relocation,
                period=period,
                date_from=date_from,
                date_to=date_to,
                age_from=age_from,
                age_to=age_to,
                gender=gender,
                experience=experience,
                skill=skill,
                language=language,
                label=label,
                currency=currency,
                salary_from=salary_from,
                salary_to=salary_to,
                professional_role=professional_role,
                citizenship=citizenship,
                work_ticket=work_ticket,
                educational_institution=educational_institution,
                driver_license_types=driver_license_types,
                search_in_responses=search_in_responses,
                by_text_prefix=by_text_prefix,
                order_by=order_by,
                page=page,
                per_page=per_page,
                employment_form=employment_form,
                work_format=work_format,
                education_levels=education_levels,
                job_search_status=job_search_status,
                business_trip_readiness=business_trip_readiness,
                district=district,
                filter_exp_industry=filter_exp_industry,
                filter_exp_period=filter_exp_period,
                vacancy_id=vacancy_id,
                resume=resume,
                folder=folder,
                include_all_folders=include_all_folders,
                with_job_search_status=with_job_search_status,
                saved_search_id=saved_search_id,
                search_by_vacancy_id=search_by_vacancy_id,
                last_used=last_used,
                last_used_timestamp=last_used_timestamp,
            )
        )

    async def create_saved_resume_search(
        self,
        *,
        text: list[ResumeSearchText] | None = None,
        area: list[int | str] | None = None,
        metro: list[int | str] | None = None,
        relocation: str | None = None,
        period: int | None = None,
        date_from: date | datetime | None = None,
        date_to: date | datetime | None = None,
        age_from: int | None = None,
        age_to: int | None = None,
        gender: str | None = None,
        experience: list[str] | None = None,
        skill: list[int | str] | None = None,
        language: list[str] | None = None,
        label: list[str] | None = None,
        currency: str | None = None,
        salary_from: int | None = None,
        salary_to: int | None = None,
        professional_role: list[int | str] | None = None,
        citizenship: list[int | str] | None = None,
        work_ticket: list[int | str] | None = None,
        educational_institution: list[int | str] | None = None,
        driver_license_types: list[str] | None = None,
        search_in_responses: bool | None = None,
        by_text_prefix: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        employment_form: list[str] | None = None,
        work_format: list[str] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            CreateSavedResumeSearch(
                host=host,
                locale=locale,
                text=text,
                area=area,
                metro=metro,
                relocation=relocation,
                period=period,
                date_from=date_from,
                date_to=date_to,
                age_from=age_from,
                age_to=age_to,
                gender=gender,
                experience=experience,
                skill=skill,
                language=language,
                label=label,
                currency=currency,
                salary_from=salary_from,
                salary_to=salary_to,
                professional_role=professional_role,
                citizenship=citizenship,
                work_ticket=work_ticket,
                educational_institution=educational_institution,
                driver_license_types=driver_license_types,
                search_in_responses=search_in_responses,
                by_text_prefix=by_text_prefix,
                order_by=order_by,
                page=page,
                per_page=per_page,
                employment_form=employment_form,
                work_format=work_format,
            )
        )

    async def get_resume(
        self,
        resume_id: str,
        *,
        with_negotiations_history: bool | None = None,
        with_creds: bool | None = None,
        with_job_search_status: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Resume:
        return await self(
            GetResume(
                host=host,
                locale=locale,
                resume_id=resume_id,
                with_negotiations_history=with_negotiations_history,
                with_creds=with_creds,
                with_job_search_status=with_job_search_status,
            )
        )

    async def get_resume_negotiations_history(
        self,
        resume_id: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> NegotiationsHistory:
        return await self(
            GetResumeNegotiationsHistory(host=host, locale=locale, resume_id=resume_id)
        )

    async def get_vacancy_visitors(
        self,
        vacancy_id: int | str,
        *,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VisitorsPage:
        return await self(
            GetVacancyVisitors(
                host=host,
                locale=locale,
                vacancy_id=vacancy_id,
                page=page,
                per_page=per_page,
            )
        )

    async def get_saved_resume_searches(
        self,
        *,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[SavedResumeSearch]:
        return await self(
            GetSavedResumeSearches(
                host=host, locale=locale, page=page, per_page=per_page
            )
        )

    async def get_saved_resume_search(
        self,
        saved_search_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> SavedResumeSearch:
        return await self(
            GetSavedResumeSearch(
                host=host, locale=locale, saved_search_id=saved_search_id
            )
        )

    async def update_saved_resume_search(
        self,
        saved_search_id: int | str,
        *,
        name: str | None = None,
        subscription: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            UpdateSavedResumeSearch(
                host=host,
                locale=locale,
                saved_search_id=saved_search_id,
                name=name,
                subscription=subscription,
            )
        )

    async def delete_saved_resume_search(
        self,
        saved_search_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteSavedResumeSearch(
                host=host, locale=locale, saved_search_id=saved_search_id
            )
        )

    async def move_saved_resume_search(
        self,
        saved_search_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            MoveSavedResumeSearch(
                host=host,
                locale=locale,
                saved_search_id=saved_search_id,
                manager_id=manager_id,
            )
        )

    async def get_negotiation_collections(
        self,
        *,
        vacancy_id: int | str | None = None,
        status: str | None = None,
        has_updates: bool | None = None,
        with_job_search_status: bool | None = None,
        with_generated_collections: bool | None = None,
        order_by: str | None = None,
        order: Literal["asc", "desc"] | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> NegotiationsCollections:
        return await self(
            GetNegotiationCollections(
                host=host,
                locale=locale,
                vacancy_id=vacancy_id,
                status=status,
                has_updates=has_updates,
                with_job_search_status=with_job_search_status,
                with_generated_collections=with_generated_collections,
                order_by=order_by,
                order=order,
                page=page,
                per_page=per_page,
            )
        )

    async def get_collection_negotiations(
        self,
        vacancy_id: int | str,
        *,
        collection_name: str = "response",
        search_text: str | None = None,
        age_from: int | None = None,
        age_to: int | None = None,
        area: list[int | str] | None = None,
        citizenship: list[int | str] | None = None,
        currency: str | None = None,
        salary_from: int | None = None,
        salary_to: int | None = None,
        driver_license_types: list[str] | None = None,
        educational_institution: list[int | str] | None = None,
        education_level: str | None = None,
        experience: list[str] | None = None,
        gender: str | None = None,
        language: list[str] | None = None,
        relocation: str | None = None,
        search_radius_meters: int | None = None,
        show_only_new: bool | None = None,
        show_only_new_responses: bool | None = None,
        show_only_with_vehicle: bool | None = None,
        show_only_with_medical_book: bool | None = None,
        show_only_with_self_employment: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> NegotiationsPage:
        return await self(
            GetCollectionNegotiations(
                host=host,
                locale=locale,
                vacancy_id=vacancy_id,
                collection_name=collection_name,
                search_text=search_text,
                age_from=age_from,
                age_to=age_to,
                area=area,
                citizenship=citizenship,
                currency=currency,
                salary_from=salary_from,
                salary_to=salary_to,
                driver_license_types=driver_license_types,
                educational_institution=educational_institution,
                education_level=education_level,
                experience=experience,
                gender=gender,
                language=language,
                relocation=relocation,
                search_radius_meters=search_radius_meters,
                show_only_new=show_only_new,
                show_only_new_responses=show_only_new_responses,
                show_only_with_vehicle=show_only_with_vehicle,
                show_only_with_medical_book=show_only_with_medical_book,
                show_only_with_self_employment=show_only_with_self_employment,
                order_by=order_by,
                page=page,
                per_page=per_page,
            )
        )

    async def get_negotiation(
        self,
        negotiation_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Negotiation:
        return await self(
            GetNegotiation(host=host, locale=locale, negotiation_id=negotiation_id)
        )

    async def move_negotiation(
        self,
        collection_name: str,
        topic_id: int | str,
        *,
        message: str | None = None,
        send_sms: bool | None = None,
        address_id: int | str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            MoveNegotiation(
                host=host,
                locale=locale,
                collection_name=collection_name,
                topic_id=topic_id,
                message=message,
                send_sms=send_sms,
                address_id=address_id,
            )
        )

    async def change_negotiation_state(
        self,
        collection_name: str,
        negotiation_id: int | str,
        *,
        message: str | None = None,
        send_sms: bool | None = None,
        address_id: int | str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            ChangeNegotiationState(
                host=host,
                locale=locale,
                collection_name=collection_name,
                negotiation_id=negotiation_id,
                message=message,
                send_sms=send_sms,
                address_id=address_id,
            )
        )

    async def mark_negotiations_read(
        self,
        topic_id: list[int | str],
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            MarkNegotiationsRead(host=host, locale=locale, topic_id=topic_id)
        )

    async def get_negotiation_messages(
        self,
        negotiation_id: int | str,
        *,
        with_text_only: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[NegotiationMessage]:
        return await self(
            GetNegotiationMessages(
                host=host,
                locale=locale,
                negotiation_id=negotiation_id,
                with_text_only=with_text_only,
                page=page,
                per_page=per_page,
            )
        )

    async def get_negotiation_test_result(
        self,
        negotiation_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> NegotiationTestResult:
        return await self(
            GetNegotiationTestResult(
                host=host, locale=locale, negotiation_id=negotiation_id
            )
        )

    async def invite_applicant(
        self,
        vacancy_id: int | str,
        resume_id: str,
        *,
        message: str | None = None,
        send_sms: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            InviteApplicant(
                host=host,
                locale=locale,
                vacancy_id=vacancy_id,
                resume_id=resume_id,
                message=message,
                send_sms=send_sms,
            )
        )

    async def get_employer_negotiations_statistics(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> EmployerNegotiationsStatistics:
        return await self(
            GetEmployerNegotiationsStatistics(
                host=host, locale=locale, employer_id=employer_id
            )
        )

    async def get_manager_negotiations_statistics(
        self,
        employer_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ManagerNegotiationsStatistics:
        return await self(
            GetManagerNegotiationsStatistics(
                host=host, locale=locale, employer_id=employer_id, manager_id=manager_id
            )
        )

    async def get_message_templates(
        self,
        template: str,
        *,
        topic_id: int | str | None = None,
        vacancy_id: int | str | None = None,
        resume_id: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> MessageTemplates:
        return await self(
            GetMessageTemplates(
                host=host,
                locale=locale,
                template=template,
                topic_id=topic_id,
                vacancy_id=vacancy_id,
                resume_id=resume_id,
            )
        )

    async def get_mail_templates(
        self,
        employer_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[MailTemplate]:
        return await self(
            GetMailTemplates(host=host, locale=locale, employer_id=employer_id)
        )

    async def update_mail_template(
        self,
        employer_id: int | str,
        template_id: int | str,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            UpdateMailTemplate(
                host=host,
                locale=locale,
                employer_id=employer_id,
                template_id=template_id,
                text=text,
            )
        )

    async def get_applicant_comments(
        self,
        applicant_id: int | str,
        *,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[ApplicantComment]:
        return await self(
            GetApplicantComments(
                host=host,
                locale=locale,
                applicant_id=applicant_id,
                order_by=order_by,
                page=page,
                per_page=per_page,
            )
        )

    async def add_applicant_comment(
        self,
        applicant_id: int | str,
        text: str,
        access_type: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ApplicantComment:
        return await self(
            AddApplicantComment(
                host=host,
                locale=locale,
                applicant_id=applicant_id,
                text=text,
                access_type=access_type,
            )
        )

    async def update_applicant_comment(
        self,
        applicant_id: int | str,
        comment_id: int | str,
        *,
        text: str | None = None,
        access_type: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            UpdateApplicantComment(
                host=host,
                locale=locale,
                applicant_id=applicant_id,
                comment_id=comment_id,
                text=text,
                access_type=access_type,
            )
        )

    async def delete_applicant_comment(
        self,
        applicant_id: int | str,
        comment_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteApplicantComment(
                host=host,
                locale=locale,
                applicant_id=applicant_id,
                comment_id=comment_id,
            )
        )

    async def publish_vacancy(
        self,
        name: str,
        description: str,
        area: Id,
        vacancy_properties: VacancyPropertiesInput,
        *,
        code: str | None = None,
        custom_employer_name: str | None = None,
        department: Id | None = None,
        address: VacancyAddressInput | None = None,
        contacts: Contacts | None = None,
        show_contacts: bool | None = None,
        salary_range: SalaryRangeInput | None = None,
        experience: Id | None = None,
        employment_form: Id | None = None,
        work_format: list[Id] | None = None,
        work_schedule_by_days: list[Id] | None = None,
        working_hours: list[Id] | None = None,
        fly_in_fly_out_duration: list[Id] | None = None,
        civil_law_contracts: list[Id] | None = None,
        professional_roles: list[Id] | None = None,
        key_skills: list[KeySkill] | None = None,
        languages: list[VacancyLanguageInput] | None = None,
        driver_license_types: list[Id] | None = None,
        age_restriction: Id | None = None,
        branded_template: Id | None = None,
        test: VacancyTest | None = None,
        auto_response: AutoResponse | None = None,
        allow_messages: bool | None = None,
        response_url: str | None = None,
        response_letter_required: bool | None = None,
        response_notifications: bool | None = None,
        accept_incomplete_resumes: bool | None = None,
        accept_labor_contract: bool | None = None,
        internship: bool | None = None,
        night_shifts: bool | None = None,
        inclusiveness_description: str | None = None,
        inclusiveness_types: list[str] | None = None,
        manager: Id | None = None,
        employer_service_id: str | None = None,
        previous_id: str | None = None,
        closed_for_applicants: bool | None = None,
        ignore_duplicates: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Id:
        return await self(
            PublishVacancy(
                host=host,
                locale=locale,
                code=code,
                custom_employer_name=custom_employer_name,
                department=department,
                address=address,
                contacts=contacts,
                show_contacts=show_contacts,
                salary_range=salary_range,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                fly_in_fly_out_duration=fly_in_fly_out_duration,
                civil_law_contracts=civil_law_contracts,
                professional_roles=professional_roles,
                key_skills=key_skills,
                languages=languages,
                driver_license_types=driver_license_types,
                age_restriction=age_restriction,
                branded_template=branded_template,
                test=test,
                auto_response=auto_response,
                allow_messages=allow_messages,
                response_url=response_url,
                response_letter_required=response_letter_required,
                response_notifications=response_notifications,
                accept_incomplete_resumes=accept_incomplete_resumes,
                accept_labor_contract=accept_labor_contract,
                internship=internship,
                night_shifts=night_shifts,
                inclusiveness_description=inclusiveness_description,
                inclusiveness_types=inclusiveness_types,
                name=name,
                description=description,
                area=area,
                vacancy_properties=vacancy_properties,
                manager=manager,
                employer_service_id=employer_service_id,
                previous_id=previous_id,
                closed_for_applicants=closed_for_applicants,
                ignore_duplicates=ignore_duplicates,
            )
        )

    async def edit_vacancy(
        self,
        vacancy_id: int | str,
        *,
        code: str | None = None,
        custom_employer_name: str | None = None,
        department: Id | None = None,
        address: VacancyAddressInput | None = None,
        contacts: Contacts | None = None,
        show_contacts: bool | None = None,
        salary_range: SalaryRangeInput | None = None,
        experience: Id | None = None,
        employment_form: Id | None = None,
        work_format: list[Id] | None = None,
        work_schedule_by_days: list[Id] | None = None,
        working_hours: list[Id] | None = None,
        fly_in_fly_out_duration: list[Id] | None = None,
        civil_law_contracts: list[Id] | None = None,
        professional_roles: list[Id] | None = None,
        key_skills: list[KeySkill] | None = None,
        languages: list[VacancyLanguageInput] | None = None,
        driver_license_types: list[Id] | None = None,
        age_restriction: Id | None = None,
        branded_template: Id | None = None,
        test: VacancyTest | None = None,
        auto_response: AutoResponse | None = None,
        allow_messages: bool | None = None,
        response_url: str | None = None,
        response_letter_required: bool | None = None,
        response_notifications: bool | None = None,
        accept_incomplete_resumes: bool | None = None,
        accept_labor_contract: bool | None = None,
        internship: bool | None = None,
        night_shifts: bool | None = None,
        inclusiveness_description: str | None = None,
        inclusiveness_types: list[str] | None = None,
        name: str | None = None,
        description: str | None = None,
        vacancy_properties: VacancyPropertiesInput | None = None,
        manager: Id | None = None,
        ignore_duplicates: bool | None = None,
        ignore_replacement_warning: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            EditVacancy(
                host=host,
                locale=locale,
                code=code,
                custom_employer_name=custom_employer_name,
                department=department,
                address=address,
                contacts=contacts,
                show_contacts=show_contacts,
                salary_range=salary_range,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                fly_in_fly_out_duration=fly_in_fly_out_duration,
                civil_law_contracts=civil_law_contracts,
                professional_roles=professional_roles,
                key_skills=key_skills,
                languages=languages,
                driver_license_types=driver_license_types,
                age_restriction=age_restriction,
                branded_template=branded_template,
                test=test,
                auto_response=auto_response,
                allow_messages=allow_messages,
                response_url=response_url,
                response_letter_required=response_letter_required,
                response_notifications=response_notifications,
                accept_incomplete_resumes=accept_incomplete_resumes,
                accept_labor_contract=accept_labor_contract,
                internship=internship,
                night_shifts=night_shifts,
                inclusiveness_description=inclusiveness_description,
                inclusiveness_types=inclusiveness_types,
                vacancy_id=vacancy_id,
                name=name,
                description=description,
                vacancy_properties=vacancy_properties,
                manager=manager,
                ignore_duplicates=ignore_duplicates,
                ignore_replacement_warning=ignore_replacement_warning,
            )
        )

    async def get_vacancy_prolongation(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacancyProlongation:
        return await self(
            GetVacancyProlongation(host=host, locale=locale, vacancy_id=vacancy_id)
        )

    async def prolongate_vacancy(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            ProlongateVacancy(host=host, locale=locale, vacancy_id=vacancy_id)
        )

    async def get_active_vacancies(
        self,
        employer_id: int | str,
        *,
        text: str | None = None,
        area: int | str | None = None,
        manager_ids: list[int | str] | None = None,
        department_id: str | None = None,
        resume_id: str | None = None,
        all_accessible: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerVacancy]:
        return await self(
            GetActiveVacancies(
                host=host,
                locale=locale,
                employer_id=employer_id,
                text=text,
                area=area,
                manager_ids=manager_ids,
                department_id=department_id,
                resume_id=resume_id,
                all_accessible=all_accessible,
                order_by=order_by,
                page=page,
                per_page=per_page,
            )
        )

    async def get_archived_vacancies(
        self,
        employer_id: int | str,
        *,
        manager_id: list[int | str] | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerVacancy]:
        return await self(
            GetArchivedVacancies(
                host=host,
                locale=locale,
                employer_id=employer_id,
                manager_id=manager_id,
                order_by=order_by,
                page=page,
                per_page=per_page,
            )
        )

    async def archive_vacancy(
        self,
        employer_id: int | str,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            ArchiveVacancy(
                host=host, locale=locale, employer_id=employer_id, vacancy_id=vacancy_id
            )
        )

    async def get_hidden_vacancies(
        self,
        employer_id: int | str,
        *,
        manager_id: list[int | str] | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[EmployerVacancy]:
        return await self(
            GetHiddenVacancies(
                host=host,
                locale=locale,
                employer_id=employer_id,
                manager_id=manager_id,
                order_by=order_by,
                page=page,
                per_page=per_page,
            )
        )

    async def hide_vacancy(
        self,
        employer_id: int | str,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            HideVacancy(
                host=host, locale=locale, employer_id=employer_id, vacancy_id=vacancy_id
            )
        )

    async def restore_vacancy(
        self,
        employer_id: int | str,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            RestoreVacancy(
                host=host, locale=locale, employer_id=employer_id, vacancy_id=vacancy_id
            )
        )

    async def get_vacancy_upgrades(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacancyUpgrades:
        return await self(
            GetVacancyUpgrades(host=host, locale=locale, vacancy_id=vacancy_id)
        )

    async def get_vacancy_stats(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[VacancyStatsItem]:
        return await self(
            GetVacancyStats(host=host, locale=locale, vacancy_id=vacancy_id)
        )

    async def get_vacancy_conditions(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> dict[str, VacancyFieldCondition | None]:
        return await self(GetVacancyConditions(host=host, locale=locale))

    async def get_preferred_negotiations_order(
        self,
        vacancy_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> PreferredNegotiationsOrder:
        return await self(
            GetPreferredNegotiationsOrder(
                host=host, locale=locale, vacancy_id=vacancy_id
            )
        )

    async def set_preferred_negotiations_order(
        self,
        vacancy_id: int | str,
        order: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            SetPreferredNegotiationsOrder(
                host=host, locale=locale, vacancy_id=vacancy_id, order=order
            )
        )

    async def get_vacancy_drafts(
        self,
        *,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[VacancyDraftItem]:
        return await self(
            GetVacancyDrafts(host=host, locale=locale, page=page, per_page=per_page)
        )

    async def create_vacancy_draft(
        self,
        *,
        code: str | None = None,
        custom_employer_name: str | None = None,
        department: Id | None = None,
        address: VacancyAddressInput | None = None,
        contacts: Contacts | None = None,
        show_contacts: bool | None = None,
        salary_range: SalaryRangeInput | None = None,
        experience: Id | None = None,
        employment_form: Id | None = None,
        work_format: list[Id] | None = None,
        work_schedule_by_days: list[Id] | None = None,
        working_hours: list[Id] | None = None,
        fly_in_fly_out_duration: list[Id] | None = None,
        civil_law_contracts: list[Id] | None = None,
        professional_roles: list[Id] | None = None,
        key_skills: list[KeySkill] | None = None,
        languages: list[VacancyLanguageInput] | None = None,
        driver_license_types: list[Id] | None = None,
        age_restriction: Id | None = None,
        branded_template: Id | None = None,
        test: VacancyTest | None = None,
        auto_response: AutoResponse | None = None,
        allow_messages: bool | None = None,
        response_url: str | None = None,
        response_letter_required: bool | None = None,
        response_notifications: bool | None = None,
        accept_incomplete_resumes: bool | None = None,
        accept_labor_contract: bool | None = None,
        internship: bool | None = None,
        night_shifts: bool | None = None,
        inclusiveness_description: str | None = None,
        inclusiveness_types: list[str] | None = None,
        name: str | None = None,
        description: str | None = None,
        area: Id | None = None,
        areas: list[Id] | None = None,
        assigned_manager_id: str | None = None,
        employer_service_id: str | None = None,
        scheduled_at: datetime | None = None,
        closed_for_applicants: bool | None = None,
        vacancy_properties: VacancyPropertiesInput | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> DraftResponse:
        return await self(
            CreateVacancyDraft(
                host=host,
                locale=locale,
                code=code,
                custom_employer_name=custom_employer_name,
                department=department,
                address=address,
                contacts=contacts,
                show_contacts=show_contacts,
                salary_range=salary_range,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                fly_in_fly_out_duration=fly_in_fly_out_duration,
                civil_law_contracts=civil_law_contracts,
                professional_roles=professional_roles,
                key_skills=key_skills,
                languages=languages,
                driver_license_types=driver_license_types,
                age_restriction=age_restriction,
                branded_template=branded_template,
                test=test,
                auto_response=auto_response,
                allow_messages=allow_messages,
                response_url=response_url,
                response_letter_required=response_letter_required,
                response_notifications=response_notifications,
                accept_incomplete_resumes=accept_incomplete_resumes,
                accept_labor_contract=accept_labor_contract,
                internship=internship,
                night_shifts=night_shifts,
                inclusiveness_description=inclusiveness_description,
                inclusiveness_types=inclusiveness_types,
                name=name,
                description=description,
                area=area,
                areas=areas,
                assigned_manager_id=assigned_manager_id,
                employer_service_id=employer_service_id,
                scheduled_at=scheduled_at,
                closed_for_applicants=closed_for_applicants,
                vacancy_properties=vacancy_properties,
            )
        )

    async def get_vacancy_draft(
        self,
        draft_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacancyDraft:
        return await self(GetVacancyDraft(host=host, locale=locale, draft_id=draft_id))

    async def edit_vacancy_draft(
        self,
        draft_id: int | str,
        *,
        code: str | None = None,
        custom_employer_name: str | None = None,
        department: Id | None = None,
        address: VacancyAddressInput | None = None,
        contacts: Contacts | None = None,
        show_contacts: bool | None = None,
        salary_range: SalaryRangeInput | None = None,
        experience: Id | None = None,
        employment_form: Id | None = None,
        work_format: list[Id] | None = None,
        work_schedule_by_days: list[Id] | None = None,
        working_hours: list[Id] | None = None,
        fly_in_fly_out_duration: list[Id] | None = None,
        civil_law_contracts: list[Id] | None = None,
        professional_roles: list[Id] | None = None,
        key_skills: list[KeySkill] | None = None,
        languages: list[VacancyLanguageInput] | None = None,
        driver_license_types: list[Id] | None = None,
        age_restriction: Id | None = None,
        branded_template: Id | None = None,
        test: VacancyTest | None = None,
        auto_response: AutoResponse | None = None,
        allow_messages: bool | None = None,
        response_url: str | None = None,
        response_letter_required: bool | None = None,
        response_notifications: bool | None = None,
        accept_incomplete_resumes: bool | None = None,
        accept_labor_contract: bool | None = None,
        internship: bool | None = None,
        night_shifts: bool | None = None,
        inclusiveness_description: str | None = None,
        inclusiveness_types: list[str] | None = None,
        name: str | None = None,
        description: str | None = None,
        area: Id | None = None,
        areas: list[Id] | None = None,
        assigned_manager_id: str | None = None,
        employer_service_id: str | None = None,
        scheduled_at: datetime | None = None,
        closed_for_applicants: bool | None = None,
        vacancy_properties: VacancyPropertiesInput | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> DraftResponse:
        return await self(
            EditVacancyDraft(
                host=host,
                locale=locale,
                code=code,
                custom_employer_name=custom_employer_name,
                department=department,
                address=address,
                contacts=contacts,
                show_contacts=show_contacts,
                salary_range=salary_range,
                experience=experience,
                employment_form=employment_form,
                work_format=work_format,
                work_schedule_by_days=work_schedule_by_days,
                working_hours=working_hours,
                fly_in_fly_out_duration=fly_in_fly_out_duration,
                civil_law_contracts=civil_law_contracts,
                professional_roles=professional_roles,
                key_skills=key_skills,
                languages=languages,
                driver_license_types=driver_license_types,
                age_restriction=age_restriction,
                branded_template=branded_template,
                test=test,
                auto_response=auto_response,
                allow_messages=allow_messages,
                response_url=response_url,
                response_letter_required=response_letter_required,
                response_notifications=response_notifications,
                accept_incomplete_resumes=accept_incomplete_resumes,
                accept_labor_contract=accept_labor_contract,
                internship=internship,
                night_shifts=night_shifts,
                inclusiveness_description=inclusiveness_description,
                inclusiveness_types=inclusiveness_types,
                draft_id=draft_id,
                name=name,
                description=description,
                area=area,
                areas=areas,
                assigned_manager_id=assigned_manager_id,
                employer_service_id=employer_service_id,
                scheduled_at=scheduled_at,
                closed_for_applicants=closed_for_applicants,
                vacancy_properties=vacancy_properties,
            )
        )

    async def delete_vacancy_draft(
        self,
        draft_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteVacancyDraft(host=host, locale=locale, draft_id=draft_id)
        )

    async def get_vacancy_draft_duplicates(
        self,
        draft_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> VacancyDuplicates:
        return await self(
            GetVacancyDraftDuplicates(host=host, locale=locale, draft_id=draft_id)
        )

    async def publish_vacancy_draft(
        self,
        draft_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> PublishedDraft:
        return await self(
            PublishVacancyDraft(host=host, locale=locale, draft_id=draft_id)
        )

    async def disable_draft_auto_publication(
        self,
        draft_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DisableDraftAutoPublication(host=host, locale=locale, draft_id=draft_id)
        )

    async def get_chats(
        self,
        *,
        filter_unread: bool | None = None,
        filter_has_text_message: bool | None = None,
        vacancy_status: Literal["all", "with", "without"] | None = None,
        filter_with_vacancy_ids: list[int | str] | None = None,
        page: int | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Page[Chat]:
        return await self(
            GetChats(
                host=host,
                locale=locale,
                filter_unread=filter_unread,
                filter_has_text_message=filter_has_text_message,
                vacancy_status=vacancy_status,
                filter_with_vacancy_ids=filter_with_vacancy_ids,
                page=page,
                per_page=per_page,
            )
        )

    async def get_unread_chats_count(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> UnreadChatsCount:
        return await self(GetUnreadChatsCount(host=host, locale=locale))

    async def create_chat_without_vacancy(
        self,
        resume_hash: str,
        *,
        first_message: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> dict[str, Any]:
        return await self(
            CreateChatWithoutVacancy(
                host=host,
                locale=locale,
                resume_hash=resume_hash,
                first_message=first_message,
            )
        )

    async def get_chat_messages(
        self,
        chat_id: int | str,
        *,
        start_message_id: int | str | None = None,
        limit: int | None = None,
        order: Literal["prev", "next"] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ChatMessages:
        return await self(
            GetChatMessages(
                host=host,
                locale=locale,
                chat_id=chat_id,
                start_message_id=start_message_id,
                limit=limit,
                order=order,
            )
        )

    async def send_chat_message(
        self,
        chat_id: int | str,
        *,
        text: str | None = None,
        file_upload_ids: list[str] | None = None,
        is_automated: bool | None = None,
        idempotency_key: str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Id:
        return await self(
            SendChatMessage(
                host=host,
                locale=locale,
                chat_id=chat_id,
                text=text,
                file_upload_ids=file_upload_ids,
                is_automated=is_automated,
                idempotency_key=idempotency_key,
            )
        )

    async def edit_chat_message(
        self,
        chat_id: int | str,
        message_id: int | str,
        text: str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            EditChatMessage(
                host=host,
                locale=locale,
                chat_id=chat_id,
                message_id=message_id,
                text=text,
            )
        )

    async def delete_chat_message(
        self,
        chat_id: int | str,
        message_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteChatMessage(
                host=host, locale=locale, chat_id=chat_id, message_id=message_id
            )
        )

    async def mark_chat_message_read(
        self,
        chat_id: int | str,
        message_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            MarkChatMessageRead(
                host=host, locale=locale, chat_id=chat_id, message_id=message_id
            )
        )

    async def leave_chat(
        self,
        chat_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(LeaveChat(host=host, locale=locale, chat_id=chat_id))

    async def set_chat_write_possibility(
        self,
        chat_id: int | str,
        applicant_write_possibility: bool,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            SetChatWritePossibility(
                host=host,
                locale=locale,
                chat_id=chat_id,
                applicant_write_possibility=applicant_write_possibility,
            )
        )

    async def get_chat_participants(
        self,
        chat_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[ChatParticipant]:
        return await self(
            GetChatParticipants(host=host, locale=locale, chat_id=chat_id)
        )

    async def add_chat_participant(
        self,
        chat_id: int | str,
        manager_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            AddChatParticipant(
                host=host, locale=locale, chat_id=chat_id, manager_id=manager_id
            )
        )

    async def get_chat_file_upload_link(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ChatFileUploadLink:
        return await self(GetChatFileUploadLink(host=host, locale=locale))

    async def get_chat_files_conditions(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> ChatFilesConditions:
        return await self(GetChatFilesConditions(host=host, locale=locale))

    async def get_webhook_subscriptions(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[WebhookSubscription]:
        return await self(GetWebhookSubscriptions(host=host, locale=locale))

    async def create_webhook_subscription(
        self,
        url: str,
        actions: list[WebhookAction],
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Id:
        return await self(
            CreateWebhookSubscription(
                host=host, locale=locale, url=url, actions=actions
            )
        )

    async def update_webhook_subscription(
        self,
        subscription_id: int | str,
        *,
        url: str | None = None,
        actions: list[WebhookAction] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            UpdateWebhookSubscription(
                host=host,
                locale=locale,
                subscription_id=subscription_id,
                url=url,
                actions=actions,
            )
        )

    async def delete_webhook_subscription(
        self,
        subscription_id: int | str,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> None:
        return await self(
            DeleteWebhookSubscription(
                host=host, locale=locale, subscription_id=subscription_id
            )
        )

    async def get_calls_history(
        self,
        *,
        vacancy_id: list[int | str] | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
        direction: Literal["outgoing", "incoming"] | None = None,
        successful: bool | None = None,
        with_resume: bool | None = None,
        without_vacancy: bool | None = None,
        link_id: str | None = None,
        next_cursor: str | None = None,
        previous_cursor: str | None = None,
        per_page: int | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> CallsHistory:
        return await self(
            GetCallsHistory(
                host=host,
                locale=locale,
                vacancy_id=vacancy_id,
                date_from=date_from,
                date_to=date_to,
                direction=direction,
                successful=successful,
                with_resume=with_resume,
                without_vacancy=without_vacancy,
                link_id=link_id,
                next_cursor=next_cursor,
                previous_cursor=previous_cursor,
                per_page=per_page,
            )
        )

    async def get_call_link(
        self,
        resume_id: str,
        *,
        vacancy_id: int | str | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> CallLink:
        return await self(
            GetCallLink(
                host=host, locale=locale, resume_id=resume_id, vacancy_id=vacancy_id
            )
        )

    async def search_call_transcripts(
        self,
        *,
        call_ids: list[str] | None = None,
        link_ids: list[str] | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> CallTranscripts:
        return await self(
            SearchCallTranscripts(
                host=host, locale=locale, call_ids=call_ids, link_ids=link_ids
            )
        )

    async def get_clickme_statistics(
        self,
        date_from: date,
        date_to: date,
        *,
        with_banners: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> Items[ClickmeStatisticsItem]:
        return await self(
            GetClickmeStatistics(
                host=host,
                locale=locale,
                date_from=date_from,
                date_to=date_to,
                with_banners=with_banners,
            )
        )

    async def get_salary_evaluation(
        self,
        area_id: int | str,
        *,
        exclude_area: list[int | str] | None = None,
        employee_level: list[int | str] | None = None,
        industry: list[int | str] | None = None,
        speciality: list[int | str] | None = None,
        position_name: str | None = None,
        extend_sources: bool | None = None,
        host: Host | None = None,
        locale: str | None = None,
    ) -> SalaryEvaluation:
        return await self(
            GetSalaryEvaluation(
                host=host,
                locale=locale,
                area_id=area_id,
                exclude_area=exclude_area,
                employee_level=employee_level,
                industry=industry,
                speciality=speciality,
                position_name=position_name,
                extend_sources=extend_sources,
            )
        )

    async def get_salary_industries(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[Industry]:
        return await self(GetSalaryIndustries(host=host, locale=locale))

    async def get_salary_professional_areas(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[SalaryProfessionalArea]:
        return await self(GetSalaryProfessionalAreas(host=host, locale=locale))

    async def get_salary_employee_levels(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[IdNameDescription]:
        return await self(GetSalaryEmployeeLevels(host=host, locale=locale))

    async def get_salary_areas(
        self,
        *,
        host: Host | None = None,
        locale: str | None = None,
    ) -> list[SalaryArea]:
        return await self(GetSalaryAreas(host=host, locale=locale))
