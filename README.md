<p align="center">
    <img height="75" src="resources/aiohh-logo.png"/>
</p>
<p align="center"><b>aiohh</b> – async api wrapper for hh.ru</p>

## Методы

Покрыты все методы публичной спецификации hh.ru, кроме помеченных устаревшими.

| Раздел | Методы |
| --- | --- |
| Авторизация | `get_user_token`, `refresh_user_token`, `get_application_token`, `invalidate_token`, `get_me` |
| Вакансии | `search_vacancies`, `get_vacancy`, `get_similar_vacancies`, `get_related_vacancies` |
| Работодатели | `search_employers`, `get_employer` |
| Справочники | `get_dictionaries`, `get_industries`, `get_professional_roles`, `get_languages`, `get_locales`, `get_resume_locales`, `get_skills`, `get_educational_institutions`, `get_faculties`, `get_districts` |
| Регионы и метро | `get_areas`, `get_area`, `get_countries`, `get_metro`, `get_city_metro` |
| Подсказки | `suggest_positions`, `suggest_vacancy_positions`, `suggest_areas`, `suggest_area_leaves`, `suggest_fields_of_study`, `suggest_professional_roles`, `suggest_companies`, `suggest_educational_institutions`, `suggest_skills`, `suggest_vacancy_search_keywords`, `suggest_resume_search_keywords` |
| Менеджеры | `get_manager_accounts`, `get_employer_managers`, `get_employer_manager`, `add_employer_manager`, `edit_employer_manager`, `delete_employer_manager`, `get_employer_manager_types`, `get_manager_resume_limits`, `get_manager_settings` |
| Информация о работодателе | `get_employer_addresses`, `get_employer_address`, `get_employer_departments`, `get_vacancy_branded_templates`, `get_employer_vacancy_areas`, `get_employer_tests` |
| Услуги работодателя | `get_employer_services`, `get_method_access`, `get_available_publications` |
| Управление вакансиями | `publish_vacancy`, `edit_vacancy`, `get_active_vacancies`, `get_archived_vacancies`, `archive_vacancy`, `get_hidden_vacancies`, `hide_vacancy`, `restore_vacancy`, `get_vacancy_prolongation`, `prolongate_vacancy`, `get_vacancy_upgrades`, `get_vacancy_stats`, `get_vacancy_visitors`, `get_vacancy_conditions`, `get_preferred_negotiations_order`, `set_preferred_negotiations_order` |
| Черновики вакансий | `get_vacancy_drafts`, `get_vacancy_draft`, `create_vacancy_draft`, `edit_vacancy_draft`, `delete_vacancy_draft`, `get_vacancy_draft_duplicates`, `publish_vacancy_draft`, `disable_draft_auto_publication` |
| Резюме | `search_resumes`, `get_resume`, `get_resume_negotiations_history` |
| Сохранённые поиски резюме | `get_saved_resume_searches`, `get_saved_resume_search`, `create_saved_resume_search`, `update_saved_resume_search`, `delete_saved_resume_search`, `move_saved_resume_search` |
| Отклики и приглашения | `get_negotiation_collections`, `get_collection_negotiations`, `get_negotiation`, `move_negotiation`, `change_negotiation_state`, `mark_negotiations_read`, `invite_applicant`, `get_negotiation_messages`, `get_negotiation_test_result`, `get_employer_negotiations_statistics`, `get_manager_negotiations_statistics` |
| Шаблоны ответов | `get_message_templates`, `get_mail_templates`, `update_mail_template` |
| Комментарии к соискателю | `get_applicant_comments`, `add_applicant_comment`, `update_applicant_comment`, `delete_applicant_comment` |
| Чаты | `get_chats`, `get_unread_chats_count`, `create_chat_without_vacancy`, `get_chat_messages`, `send_chat_message`, `edit_chat_message`, `delete_chat_message`, `mark_chat_message_read`, `leave_chat`, `set_chat_write_possibility`, `get_chat_participants`, `add_chat_participant`, `get_chat_file_upload_link`, `get_chat_files_conditions` |
| Webhooks | `get_webhook_subscriptions`, `create_webhook_subscription`, `update_webhook_subscription`, `delete_webhook_subscription` |
| Звонки | `get_calls_history`, `get_call_link`, `search_call_transcripts` |
| Статистика | `get_clickme_statistics`, `get_salary_evaluation`, `get_salary_industries`, `get_salary_professional_areas`, `get_salary_employee_levels`, `get_salary_areas` |
