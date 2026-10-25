from datetime import datetime

from aiohh.types.base import BaseType
from aiohh.types.common import IdName


class ApplicantCounters(BaseType):
    new_resume_views: int
    resumes_count: int
    unread_negotiations: int


class JobSearchStatus(BaseType):
    id: str | None = None
    name: str | None = None
    last_change_time: datetime | None = None


class UserStatuses(BaseType):
    job_search_status: JobSearchStatus | None = None


class ProfileVideoDownloadUrl(BaseType):
    url: str
    expires_at: datetime


class ProfileVideo(BaseType):
    id: str
    download_url: ProfileVideoDownloadUrl


class ProfileVideos(BaseType):
    items: list[ProfileVideo] = []


class MeEmployer(BaseType):
    id: str
    name: str
    manager_id: str | None = None


class MeManager(BaseType):
    id: str
    has_admin_rights: bool
    has_multiple_manager_accounts: bool
    is_main_contact_person: bool
    manager_settings_url: str


class PersonalManagerPhotoUrls(BaseType):
    big: str | None = None
    small: str | None = None


class PersonalManagerUnavailable(BaseType):
    until: datetime


class PersonalManager(BaseType):
    id: str
    email: str
    first_name: str
    last_name: str
    is_available: bool
    photo_urls: PersonalManagerPhotoUrls | None = None
    unavailable: PersonalManagerUnavailable | None = None


class Me(BaseType):
    auth_type: str | None = None
    is_admin: bool
    is_applicant: bool
    is_application: bool
    is_employer: bool
    is_employer_integration: bool
    id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    email: str | None = None
    phone: str | None = None
    counters: ApplicantCounters | None = None
    is_in_search: bool | None = None
    linked_socials: list[IdName] | None = None
    negotiations_url: str | None = None
    resumes_url: str | None = None
    profile_videos: ProfileVideos | None = None
    user_statuses: UserStatuses | None = None
    employer: MeEmployer | None = None
    manager: MeManager | None = None
    personal_manager: PersonalManager | None = None
