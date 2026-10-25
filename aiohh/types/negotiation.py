from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import Id, IdName, LogoUrls, Page
from aiohh.types.resume import ResumeItem
from aiohh.types.vacancy import Address, VacancyItem


class NegotiationActionArgument(BaseType):
    id: str
    required: bool
    required_arguments: list[Id] = []


class NegotiationSubAction(BaseType):
    id: str
    name: str
    method: str
    url: str


class MessageTemplateLink(IdName):
    url: str


class NegotiationAction(BaseType):
    id: str | None = None
    name: str | None = None
    method: str | None = None
    url: str | None = None
    enabled: bool | None = None
    hidden: bool | None = None
    arguments: list[NegotiationActionArgument] = []
    sub_actions: list[NegotiationSubAction] = []
    resulting_employer_state: IdName | None = None
    templates: list[MessageTemplateLink] = []


class NegotiationsOrderType(IdName):
    url: str


class NegotiationsCollectionCounters(BaseType):
    total: int | None = None
    with_updates: int | None = None


class NegotiationsSubCollection(IdName):
    url: str
    root_collection: bool
    counters: NegotiationsCollectionCounters | None = None
    order_types: list[NegotiationsOrderType] = []


class NegotiationsCollection(IdName):
    url: str
    description: str | None = None
    hidden: bool | None = None
    counters: NegotiationsCollectionCounters | None = None
    order_types: list[NegotiationsOrderType] = []
    sub_collections: list[NegotiationsSubCollection] = []


class NegotiationsCollections(BaseType):
    collections: list[NegotiationsCollection] = []
    generated_collections: list[NegotiationsCollection] = []
    employer_states: list[IdName] = []


class NegotiationCounters(BaseType):
    messages: int | None = None
    unread_messages: int | None = None


class FunnelSubstate(BaseType):
    name: str


class FunnelStage(BaseType):
    id: str
    state: IdName
    substate: FunnelSubstate | None = None


class RelevantExperienceEmployer(BaseType):
    company_name: str | None = None
    logo_urls: LogoUrls | None = None


class RelevantExperienceItem(BaseType):
    position: str
    months: int
    employer: RelevantExperienceEmployer | None = None


class RelevantExperience(BaseType):
    experiences: list[RelevantExperienceItem] = []
    total_months: int
    outdated: bool
    outdated_months_threshold: int
    vacancy_requirements_match: bool


class ChatBotAutoSurvey(BaseType):
    text: str | None = None


class ChatBot(BaseType):
    auto_survey: ChatBotAutoSurvey | None = None


class NegotiationTestResultShort(BaseType):
    score: int
    mark: str | None = None
    url: str | None = None
    alternate_url: str | None = None


class NegotiationResume(ResumeItem):
    skill_set: list[str] | None = None
    has_vehicle: bool | None = None
    has_medical_book: bool | None = None
    has_self_employment: bool | None = None


class Negotiation(BaseType):
    id: str
    url: str | None = None
    state: IdName
    employer_state: IdName | None = None
    created_at: datetime
    updated_at: datetime
    has_updates: bool
    messaging_status: str
    viewed_by_opponent: bool
    source: str | None = None
    chat_id: int | None = None
    applicant_question_state: bool | None = None
    counters: NegotiationCounters | None = None
    professional_roles: list[Id] | None = None
    chat_bot: ChatBot | None = None
    funnel_stage: FunnelStage | None = None
    relevant_experience: RelevantExperience | None = None
    actions: list[NegotiationAction] = []
    templates: list[MessageTemplateLink] = []
    tags: list[Id] = []
    test_result: NegotiationTestResultShort | None = None
    resume: NegotiationResume | None = None
    vacancy: VacancyItem | None = None


class NegotiationsPage(Page[Negotiation]):
    ordered_by: IdName | None = None
    hidden_count: int | None = None


class NegotiationMessageAuthor(BaseType):
    participant_type: str


class AssessmentAction(IdName):
    enabled: bool
    alternate_url: str | None = None
    disable_reason: str | None = None


class Assessment(IdName):
    actions: list[AssessmentAction] = []


class NegotiationMessage(BaseType):
    id: str
    author: NegotiationMessageAuthor
    state: IdName
    text: str | None = None
    created_at: datetime
    editable: bool
    read: bool | None = None
    viewed_by_me: bool
    viewed_by_opponent: bool
    address: Address | None = None
    assessments: list[Assessment] = []


class TestClosedAnswer(BaseType):
    value: str | None = None
    selected: bool | None = None
    correct: bool | None = None


class TestOpenedAnswer(BaseType):
    value: str
    mark: str


class TestTask(BaseType):
    question: str
    closed_answers: list[TestClosedAnswer] = []
    opened_answer: TestOpenedAnswer | None = None


class TestResult(BaseType):
    name: str
    mark: str
    score: int
    duration: int
    tasks: list[TestTask] = []


class NegotiationTestResult(BaseType):
    test_result: TestResult


class Politeness(BaseType):
    index: float
    hint: str
    description: str
    article_url: str


class NegotiationsStatistics(BaseType):
    received: int
    replied_percent: float | None = None
    viewed_percent: float | None = None
    average_reply_time: float | None = None
    politeness: Politeness | None = None


class EmployerNegotiationsStatistics(BaseType):
    employer_statistics: NegotiationsStatistics


class ManagerNegotiationsStatistics(BaseType):
    manager_statistics: NegotiationsStatistics


class MessageTemplate(BaseType):
    text: str
    template_modified: bool
    employer_state: str | None = None


class MessageTemplates(BaseType):
    mail: MessageTemplate
    sms: MessageTemplate | None = None


class MailTemplate(IdName):
    text: str
    type: str
    editable: bool
    template_modified: bool
    employer_state: str | None = None
    variables: list[IdName] = []


class ApplicantCommentAuthor(BaseType):
    full_name: str


class ApplicantComment(BaseType):
    id: str
    text: str
    created_at: datetime
    is_mine: bool
    access_type: IdName
    author: ApplicantCommentAuthor
