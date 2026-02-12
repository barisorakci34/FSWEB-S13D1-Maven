# CRM Veri Sozlugu

- Uretim tarihi: 2026-02-12 08:49:34
- Kaynak dosya: `/home/ubuntu/.cursor/projects/workspace/uploads/script.txt`
- Veritabani: `katilim.crm`
- Kapsam: `Crm` semasindaki tablolar
- Toplam tablo: **213**
- Toplam kolon: **4516**
- Toplam PK kolonu: **203**
- Toplam FK baglantisi: **719**

> Not: Bu sozluk, SQL DDL scriptinden otomatik uretilmistir.

## Crm.AccountingCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Period | nvarchar(9) | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(9) | Hayir |  | Hayir |  |  |  |
| Model | nvarchar(9) | Hayir |  | Hayir |  |  |  |
| DueType | nvarchar(9) | Hayir |  | Hayir |  |  |  |
| Key | nvarchar(20) | Hayir |  | Hayir |  |  |  |
| Code | nvarchar(20) | Hayir |  | Hayir |  |  |  |
| Description | nvarchar(100) | Evet |  | Hayir |  |  |  |

## Crm.Activities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ActivityTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ActivitySubTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| Status | nvarchar(1) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ResultType | nvarchar(2) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| SuccessBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| CanceledBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsImportant | bit | Hayir |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| DescriptionDone | nvarchar(4000) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsAppointmentCall | bit | Hayir | ((0)) | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsAttendedTheMeeting | bit | Hayir | ((0)) | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsSequent | bit | Hayir | ((0)) | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ReasonDescription | nvarchar(4000) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir | Crm.Opportunities.Uid | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| OldCustomerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsSMS | bit | Hayir | ((0)) | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| IsSoundRecord | bit | Hayir | ((0)) | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| FirstAppointment | bit | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| AppointmentAssignmentUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| WillAttend | bit | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| ComplaintUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| LastMoveMesken | bit | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |
| CounterEndDate | datetime2(7) | Evet |  | Hayir |  | Crm.ActivityRecords; Crm.ActivityTypes; Crm.Contracts; Crm.Customers; Crm.DrawCodes; Crm.LeadForms; Crm.Opportunities; Crm.QualityAnswers; Crm.QualityNotes; Crm.RepPointLogs; Crm.Users |  |

## Crm.ActivityRecords

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Users |  |
| FileName | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.Users |  |
| FileSize | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.Users |  |
| ActivityUid | uniqueidentifier | Hayir |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Users |  |
| Duration | int | Evet |  | Hayir |  | Crm.Activities; Crm.Users |  |
| NewFileName | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.Users |  |

## Crm.ActivityTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| isSystem | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid | Crm.Activities; Crm.ActivityTypes; Crm.Users |  |

## Crm.AdForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.LeadForms; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.LeadForms; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.LeadForms; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.LeadForms; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| LastUpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |
| LastUpdateCount | int | Hayir | ((0)) | Hayir |  | Crm.LeadForms; Crm.Users |  |
| BlockDate | datetime2(7) | Evet |  | Hayir |  | Crm.LeadForms; Crm.Users |  |

## Crm.Advices

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Areas; Crm.Customers; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| IsDetailShared | bit | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| IsBulkInvitation | bit | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| IsProductDetail | bit | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| ProductType | varchar(1) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| ProductPrice | varchar(10) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| InstallmentPrice | varchar(10) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| AdvancePayment | varchar(10) | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| CancelledLink | bit | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| CancelledLinkDate | datetime | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| ProcessDate | datetime | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.Customers; Crm.Users |  |

## Crm.AllGroupInfo

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Name | nvarchar(20) | Hayir |  | Hayir |  |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |  |
| GroupDate | varchar(10) | Evet |  | Hayir |  |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(3) | Evet |  | Hayir |  |  |  |
| JokerCount | int | Hayir |  | Hayir |  |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |  |
| TotalSelectCount | int | Hayir |  | Hayir |  |  |  |
| ContractSelectCount | int | Hayir |  | Hayir |  |  |  |
| JokerSelectCount | int | Hayir |  | Hayir |  |  |  |
| MaxDeliveryDate | varchar(10) | Evet |  | Hayir |  |  |  |
| SelectCount | int | Hayir |  | Hayir |  |  |  |
| LastOrganizationDate | varchar(10) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| MaxDeliveryLastInstallment | int | Hayir |  | Hayir |  |  |  |
| CreatedBy | nvarchar(100) | Evet |  | Hayir |  |  |  |
| ClosedBy | nvarchar(100) | Evet |  | Hayir |  |  |  |
| StartDate | varchar(10) | Evet |  | Hayir |  |  |  |
| EndDate | varchar(10) | Evet |  | Hayir |  |  |  |
| Status | nvarchar(3) | Evet |  | Hayir |  |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |  |
| NextDraw | nvarchar(4) | Evet |  | Hayir |  |  |  |
| MaxDeliveryMonth | int | Hayir |  | Hayir |  |  |  |
| FirstOrganizationDate | varchar(10) | Evet |  | Hayir |  |  |  |
| LastDrawDate | varchar(10) | Evet |  | Hayir |  |  |  |
| NextDrawDate | varchar(10) | Evet |  | Hayir |  |  |  |
| NextDrawPeriod | nvarchar(4) | Evet |  | Hayir |  |  |  |
| BallCount | int | Hayir |  | Hayir |  |  |  |
| TotalDrawBall | int | Hayir |  | Hayir |  |  |  |

## Crm.Announcement

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Title | nvarchar(4000) | Evet |  | Hayir |  | Crm.Users |  |
| Image | nvarchar(500) | Evet |  | Hayir |  | Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.Users |  |
| ShortDescription | nvarchar(4000) | Evet |  | Hayir |  | Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Users |  |
| Channel | int | Evet |  | Hayir |  | Crm.Users |  |
| IsPopup | bit | Evet |  | Hayir |  | Crm.Users |  |
| AnnouncementType | int | Evet |  | Hayir |  | Crm.Users |  |
| AnnouncementStartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| AnnouncementEndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.ApplicationConfiguration

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Key | nvarchar(400) | Evet |  | Hayir |  |  |  |
| Value | nvarchar(max) | Evet |  | Hayir |  |  |  |
| Platform | smallint | Hayir |  | Hayir |  |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |  |

## Crm.ApplicationLoginLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| AppId | smallint | Evet |  | Hayir |  |  |  |
| PlatformId | smallint | Evet |  | Hayir |  |  |  |
| AppVersion | nvarchar(10) | Evet |  | Hayir |  |  |  |
| IsFailed | bit | Hayir |  | Hayir |  |  |  |
| Message | nvarchar(400) | Evet |  | Hayir |  |  |  |

## Crm.AppointmentAssignments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| AssignDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |
| CustomerTypeId | int | Hayir |  | Hayir |  | Crm.Customers; Crm.Leads; Crm.Organizations; Crm.Users |  |

## Crm.Areas

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| NameEn | nvarchar(100) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| Code | nvarchar(20) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| Type | nvarchar(10) | Evet |  | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |
| Point | int | Hayir | ((0)) | Hayir |  | Crm.Advices; Crm.Areas; Crm.Opportunities; Crm.OrganizationAreas; Crm.Organizations; Crm.Reps; Crm.Users |  |

## Crm.AssignedBidApprovers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Bids; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| BidUid | uniqueidentifier | Evet |  | Hayir | Crm.Bids.Uid | Crm.Bids; Crm.Users |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| ProductInstallmentCount | int | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| BidCreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |

## Crm.Authorities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Evet |  | Hayir | Crm.Roles.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| ModuleAuthUid | uniqueidentifier | Hayir |  | Hayir | Crm.ModuleAuths.Uid | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Roles; Crm.Users |  |

## Crm.BankDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Banks; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Banks; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Banks; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Banks; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Banks; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Banks; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Banks; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Evet |  | Hayir |  | Crm.Banks; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Banks; Crm.Organizations; Crm.Users |  |
| BankUid | uniqueidentifier | Evet |  | Hayir | Crm.Banks.Uid | Crm.Banks; Crm.Organizations; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.Banks; Crm.Organizations; Crm.Users |  |

## Crm.BankLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Users |  |
| MdStatus | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| TRANID | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| PAResSyntaxOK | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| MerchantID | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| MaskedCreditCard | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| sID | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ACQBIN | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Ecom_Payment_Card_ExpDate_Year | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Ecom_Payment_Card_ExpDate_Month | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| MaskedPan | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ClientIp | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| iReqDetail | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Md | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| VendorCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Storetype | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| IReqCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| MdErrorMsg | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| PAResVerified | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Cavv | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Digest | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CallbackCall | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CavvAlgorithm | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Cid | nvarchar(max) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Encoding | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Currency | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DsId | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Eci | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Version | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Clientid | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Txstatus | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Charset | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Hash | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Rnd | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| HASHPARAMS | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| HASHPARAMSVAL | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ErrMsg | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Response | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ProcReturnCode | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ErrCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| FailUrl | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| OkUrl | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Lang | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Xid | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| AuthCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| HostRefNum | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| TransId | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| HOSTMSG | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ProvisionNumber | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| HashData | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| RRN | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Stan | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ResponseMessage | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ResponseCode | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| MerchantOrderId | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| BankCode | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |

## Crm.Banks

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.BankDetails; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BankDetails; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BankDetails; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.BankDetails; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BankDetails; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BankDetails; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BankDetails; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.BankDetails; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.BankDetails; Crm.Users |  |

## Crm.BidInstallments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Bids; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Bids; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| BidUid | uniqueidentifier | Evet |  | Hayir | Crm.Bids.Uid | Crm.Bids; Crm.Users |  |
| InstallmentNumber | int | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Price | decimal(18,2) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| DueDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| IsLast | bit | Hayir |  | Hayir |  | Crm.Bids; Crm.Users |  |
| RemainingAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Editable | bit | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Sub_Type | nvarchar(10) | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |
| Sub_InstallmentNumber | int | Evet |  | Hayir |  | Crm.Bids; Crm.Users |  |

## Crm.Bids

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| SimulationUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| InstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CachePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForBranchLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForRegionLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateNotCampaign | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateNotCampaignLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServicePriceNotCampaign | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServicePriceNotCampaignLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServicePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServicePriceLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateLast | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceNewRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceNewPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceNewInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceError | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceMessage | nvarchar(500) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ReelProductInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashNewRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashNewPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashNewInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashError | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CashMessage | nvarchar(500) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| Endeks | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| Total | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductInstallmentPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductNewRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductNewPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductNewInstallmentCount | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| FirstInstallmentRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductError | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductMessage | nvarchar(4000) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryFirstInstallmentNotCampaign | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryLastInstallmentNotCampaign | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryFirstInstallmentDateNotCampaign | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DeliveryLastInstallmentDateNotCampaign | datetime2(7) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceFirstInstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| DelayingDeliveryMonth | int | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ProductLog | nvarchar(500) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsSMS | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsContract | bit | Hayir |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsActive | bit | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ApprovalRole | varchar(2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForCEO | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsDistance | bit | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsApproved | bit | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CustomerApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ConvertToContractDate | datetime2(7) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsCanBeEdited | bit | Evet | ((1)) | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceRateWithOutCashPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| MinServiceRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| MinServicePriceForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| IsFirstService | bit | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| RejectReason | nvarchar(4000) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| FirstProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| InflationIncreaseCount | int | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| PreliminaryInformationDate | datetime2(7) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| PreInfoIsApproved | bit | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| OldProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ContractDurationMonth | smallint | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| PaidInstallmentCount | smallint | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| RemainingServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| RemainingServiceInstallmentCount | smallint | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| NewContractStartDate | datetime | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| PaidServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| CachePriceAddition | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| TmsfFirmId | smallint | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| FirstServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| ServiceFirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |
| FragmentationServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.AssignedBidApprovers; Crm.BidInstallments |  |

## Crm.BranchCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.PremiumBranchRates; Crm.Premiums; Crm.Users |  |

## Crm.CampaignBranches

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| CampaignUid | uniqueidentifier | Hayir |  | Hayir | Crm.Campaigns.Uid | Crm.Campaigns; Crm.Organizations; Crm.Users |  |
| BranchUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Campaigns; Crm.Organizations; Crm.Users |  |

## Crm.CampaignItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CampaignSources; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| CampaignSourceUid | uniqueidentifier | Hayir |  | Hayir | Crm.CampaignSources.Uid | Crm.CampaignSources; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| Link | nvarchar(500) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |
| Images | nvarchar(max) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Users |  |

## Crm.CampaignName

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| CampaignNameHome | nvarchar(50) | Evet |  | Hayir |  |  |  |
| CampaignNameCar | nvarchar(50) | Evet |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Evet |  | Hayir |  |  |  |
| Uid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |

## Crm.Campaigns

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| CountOfTargetedAppeal | int | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| CountOfTargetedLead | int | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| CountOfTargetedOpportunity | int | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| TargetedPotential | decimal(18,2) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| TargetedGiro | decimal(18,2) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| Budget | decimal(18,2) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |
| Key | nvarchar(500) | Evet |  | Hayir |  | Crm.CampaignBranches; Crm.CampaignSources; Crm.Users |  |

## Crm.CampaignSources

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| CampaignUid | uniqueidentifier | Hayir |  | Hayir | Crm.Campaigns.Uid | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |
| SourceUid | uniqueidentifier | Hayir |  | Hayir | Crm.CustomerSources.Uid | Crm.CampaignItems; Crm.Campaigns; Crm.CustomerSources; Crm.Users |  |

## Crm.CashPriceIntervalRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ReelRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid | Crm.Products; Crm.Users |  |

## Crm.CodeExplanations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | int | Hayir |  | Evet |  |  | Identity |
| Description | varchar(100) | Evet |  | Hayir |  |  |  |
| Type | tinyint | Hayir |  | Hayir |  |  |  |
| No | tinyint | Hayir |  | Hayir |  |  |  |
| Code | varchar(20) | Hayir |  | Hayir |  |  |  |
| Name | varchar(100) | Hayir |  | Hayir |  |  |  |
| Explanation | varchar(100) | Evet |  | Hayir |  |  |  |

## Crm.ComplaintHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Subject | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| Explanation | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| IsAnswer | bit | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |  |
| Answer | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ComplaintUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| AssignedPersonUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |  |
| SubStatus | varchar(2) | Evet |  | Hayir |  |  |  |
| FieldNameText | nvarchar(100) | Evet |  | Hayir |  |  |  |
| OldValueText | nvarchar(100) | Evet |  | Hayir |  |  |  |
| NewValueText | nvarchar(100) | Evet |  | Hayir |  |  |  |
| TransactionName | nvarchar(100) | Evet |  | Hayir |  |  |  |
| OldValue | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| NewValue | nvarchar(4000) | Evet |  | Hayir |  |  |  |

## Crm.ComplaintNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Complaints; Crm.Users |  |
| ComplaintUid | uniqueidentifier | Hayir |  | Hayir | Crm.Complaints.Uid | Crm.Complaints; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Complaints; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Complaints; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Complaints; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Complaints; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Complaints; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Complaints; Crm.Users |  |
| Deleted | bit | Hayir | ((0)) | Hayir |  | Crm.Complaints; Crm.Users |  |
| Name | nvarchar(1000) | Evet |  | Hayir |  | Crm.Complaints; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Complaints; Crm.Users |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Complaints; Crm.Users |  |

## Crm.Complaints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Subject | nvarchar(4000) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Explanation | nvarchar(4000) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| IsAnswer | bit | Hayir |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Answer | nvarchar(4000) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Status | varchar(2) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| AssignedPersonUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Source | nvarchar(50) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Priority | nvarchar(50) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| CancellationReason | nvarchar(50) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| ComplaintNo | nvarchar(8) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| DirectCompleteDate | datetime2(7) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| SubStatus | nvarchar(2) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| Referrer | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| ReferrersDepartment | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| RelatedComplaints | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| SmsCount | int | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| OutBandCallUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| CallCount | int | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| SubjectCategoryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| SikayetvarNo | int | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |
| SikayetvarName | nvarchar(255) | Evet |  | Hayir |  | Crm.ComplaintNotes; Crm.Customers; Crm.Users |  |

## Crm.ComplaintsSubjectCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Type | char(1) | Hayir |  | Hayir |  |  |  |
| SubjectCategoryName | nvarchar(250) | Hayir |  | Hayir |  |  |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |

## Crm.ContractDocumentIssues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Description | nvarchar(max) | Evet |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Status | int | Hayir |  | Hayir |  |  |  |

## Crm.ContractIBANs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ETesisTerkinContractIbans |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| IBAN | nvarchar(150) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| BankName | nvarchar(150) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| Name | nvarchar(150) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| Surname | nvarchar(150) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| SellerIBAN | nvarchar(150) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| SellerBankName | nvarchar(250) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| FatherName | nvarchar(100) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| Type | smallint | Hayir | ((1)) | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| IsCompany | bit | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| SalesPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| SellerTckno | nvarchar(11) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |
| SellerTaxNo | nvarchar(10) | Evet |  | Hayir |  | Crm.ETesisTerkinContractIbans |  |

## Crm.ContractLeavingLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractLeavingLogType | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Department | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |

## Crm.ContractLeavings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Users |  |
| BeforeReturnContractStatus | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| BeforeReturnGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnStartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnMoneyH | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnMoneyO | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnMoneyP | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnMoneyA | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ReturnMoneyS | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InternalAudit | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InternalAuditProcessDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InternalAuditProcessedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |

## Crm.ContractProductDeliveryRange

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ContractProducts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractProducts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractProducts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractProducts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| StartMonth | int | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| EndMonth | int | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| StartMonthNotCampaign | int | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| EndMonthNotCampaign | int | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProducts; Crm.Users |  |
| ContractProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.ContractProducts.Uid | Crm.ContractProducts; Crm.Users |  |

## Crm.ContractProducts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractProductDeliveryRange; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CashRateForBranch | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ContractHtml | nvarchar(max) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| DeliveryMonth | int | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Model | nvarchar(50) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| InstallmentCount | int | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IncreaseRateAfterDelivery | decimal(18,2) | Hayir |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| FixedIndex | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| VariableIndexGroup | nvarchar(50) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| FirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Status | nvarchar(max) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| DistributedCashRate | int | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForBranchFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForRegionFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForGeneralManagerFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IsServicePriceDivided | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForCEOFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForBranchLast | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForRegionLast | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateDividedNotCampaignLast | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServiceRateDividedNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IsServicePriceDividedUntilDelivery | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| MinProductPriceForDeliveryDistributed | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IsServicePriceChargedBeforeDelivery | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceChargedBeforeDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceChargedBeforeDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceChargedBeforeDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceChargedBeforeDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceChargedBeforeDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IsServicePriceDistributed | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDistributedRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDistributedRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDistributedRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDistributedNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| MinProductPriceForDistributed | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDistributedRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| FlexibleDeliveryRate | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IsActive | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| PremiumRate | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IncreaseRateBeforeDelivery | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| IncreaseRateAfterDeliveryArray | nvarchar(max) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| MinProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| MaxProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| GroupLimit | int | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| DownPaymentUpperLimit | int | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceLoweLimit | int | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| Featured | bit | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| PointServiceRateLimit | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |
| ServicePriceDividedUntilDeliveryNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.ContractProductDeliveryRange; Crm.Users |  |

## Crm.ContractRevisions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Month | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ProccesType | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| ControllerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| ControllerDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ExtraServicePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ExtraCashPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ExtraProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| TotalExtraPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| NewDeliveryDateRange | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| NewDeliveryMonth | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeliveryLastInstallmentDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ScheduledDeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| NewContractNo | nvarchar(20) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| OldContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| TransferedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| SnapshotContractPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| Direction | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DataCorrectionType | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| RevisionAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| RevisionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DescriptionOld | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| OtherPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |

## Crm.Contracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractNo | nvarchar(450) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| GroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReelProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServicePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InstallmentCount | int | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CashRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CashPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceControllerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceControllerDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsJoker | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryMonth | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ScheduledDeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceDeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReelDeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryStartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryEndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceDeliveryControllerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceDeliveryControllerDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OperationDeliveryControllerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OperationDeliveryControllerDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CancellationReason | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CompletionReason | nvarchar(4000) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CashMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor1Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor1Tckno | nvarchar(20) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor1Phone | nvarchar(20) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor1Address | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor2Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor2Tckno | nvarchar(20) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor2Phone | nvarchar(20) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| Guarantor2Address | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractInput | varchar(max) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractOutput | varchar(max) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractProduct | varchar(max) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsOperationApproval | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsInvoice | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| RelatedContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServicePriceLast | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceRateLast | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DelayingDeliveryMonth | int | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PriceDiff | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OldGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PassiveDegree | int | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceFirstInstallmentPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InstallmentPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ExpertiseDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ExpertisePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsExpertise | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IBAN | nvarchar(150) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InvoiceDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeedDelivered | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FirstPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FirstPortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FirstOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PremiumPayment | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| BidUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FolderNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InvoiceNo | nvarchar(30) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerSurname | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerTckno | nvarchar(20) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerNo | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| GroupName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerCity | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerTown | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerHomeTown | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FinanceControllerName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioCode | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioOwner | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioOrganizationName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioOrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioParentOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioParentOrganizationName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PortfolioParentOrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerSource | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServicePricePaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CashPricePaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InstallmentPricePaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| BillPricePaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsPaid | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ColorType | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InstallmentAmount | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PaidInstallmentAmount | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| RemainingInstallmentAmount | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerPortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsPendingActivity | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CreatedByUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerCityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerTownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerHomeTownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsDistance | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsJoinJob | bit | Hayir | ((1)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DelayedInstallmentCount | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnPaymentStatus | tinyint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| SoundRecord | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsTradesman | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| GuaranteedBillGiven | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| GuaranteedBillReceived | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| LoadedBill | nvarchar(150) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| GuaranteedBillAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServiceRateWithOutCashPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerTaxNo | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| TaxNo | varchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerTaxOffice | varchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OffsetContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OffsetGiroProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OffsetGiroServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OffsetContractOffsetLogUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| NewContractOffsetLogUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CancellationDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DidBillsCome | bit | Evet | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnDescription | varchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnType | varchar(5) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnPetitionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnTransactionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CarNumberPlate | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ExpertiseValue | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeprivationOfRight | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| BillNo | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryStatus | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryDescription | nvarchar(1000) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryAppointmentDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| MeskenContractNo | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| FirstProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InflationIncreaseCount | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| LegalPursuit | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ReturnComplete | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| OffsetDelayingDeliveryMonth | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| TransferDelayingDeliveryMonth | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ProductModel | char(3) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InterimPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InterimPricePaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CustomerPhone | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| SubStatus | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DepositDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveredProductType | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractLeavingUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| StatusReasonType | varchar(5) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ManuelReconciliation | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InsuranceDeductedDeliveryPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DidPledgeAgreementCome | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| HasVPInstallment | bit | Evet | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| CanPayServicePriceInstbyVP | bit | Evet | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractProcess | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryDocumentsDeadlineDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| LogoTransferStatus | smallint | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| VPProductInstalmentCount | int | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PledgeFolderNo | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| InsurancePaymentMethod | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ConvertToPoint | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| MortgageDocumentNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| MortgagesTypeUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DidMortgageAgreementCome | bigint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| DeliveryBillsStatus | bit | Evet | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsDigitalApproval | bit | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| SendToMobileDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ContractApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PreInformationApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| MobileApprovalSender | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| AuthorizationId | varchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PersonalDataApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsStartBothInstallmentAndServiceFee | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| SendToDeliveryDocumentApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| PreviousStatus | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| IsActiveDocumentIssues | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ServicePriceCreditCardPartialCashRatio | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| NFCResult | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| SpecialProcces | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |
| ScheduledDateChangeType | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.BankLogs; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractRevisions; Crm.DataAnalysisLogs; Crm.Deliveries; Crm.DeliveryCalls; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.DrawCodes; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.Guarantors; Crm.InvoiceLogoLogs; Crm.Mortgages; Crm.NotaryLists; Crm.PosPayments; Crm.PremiumContracts; Crm.RepContracts; Crm.RepPointLogs; Crm.SmsLogs; Crm.SustainabilityReports |  |

## Crm.ContractTemplate

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Evet |  | Hayir | Crm.Products.Uid | Crm.Products; Crm.Users |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| Text | nvarchar(max) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| ProductModel | nvarchar(50) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |

## Crm.ContractTemplateVariables

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.CostForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CostDate | datetime2(7) | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| PaidDate | datetime2(7) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| IsTransfer | bit | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| Confirm | bit | Hayir |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| File | nvarchar(100) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CostTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.CostTypes.Uid | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| Name | nvarchar(200) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| ManagerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CostBudgetType | smallint | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| SubStatus | smallint | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| ApproveDate | datetime2(7) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CancelDescription | nvarchar(4000) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalRequestedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalDifferencePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| FileBankReceipt | nvarchar(100) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalPreRequestedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalProcessedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TotalPaidPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |
| CostNo | varchar(8) | Evet |  | Hayir |  | Crm.CostItems; Crm.CostTypes; Crm.Users |  |

## Crm.CostItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| CostDate | datetime2(7) | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| CostFormUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostForms.Uid | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| CostTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostTypes.Uid | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| ReceiptNo | nvarchar(100) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| TaxRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| DescriptionDetail | nvarchar(4000) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| File | nvarchar(100) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| RequestedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| AdvanceDate | datetime2(7) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| IsFirstItem | bit | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| ProcessedPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostTypes; Crm.Users |  |

## Crm.Costs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| CostTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostTypes.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| ExecutionMonth | int | Hayir |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| ExecutionYear | int | Hayir |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| Note | nvarchar(500) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| InvoiceType | nvarchar(50) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| InvoiceNumber | nvarchar(50) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| InvoiceDate | datetime2(7) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| Count | int | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |
| VAT | decimal(18,0) | Evet |  | Hayir |  | Crm.CostTypes; Crm.Organizations; Crm.Users |  |

## Crm.CostTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| IsCost | bit | Hayir | ((0)) | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| Text | nvarchar(500) | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |
| CostBudgetType | smallint | Evet |  | Hayir |  | Crm.CostForms; Crm.CostItems; Crm.Costs; Crm.Users |  |

## Crm.CustomerLoginFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Host | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.Users |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.CustomerLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| Host | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| DeviceId | varchar(200) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |
| Text | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.RepPointLogs; Crm.Users |  |

## Crm.CustomerLoginSmsFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| SmsPassword | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Host | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.Users |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.Customers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Tckno | nvarchar(11) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CustomerNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| EMail | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Address | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| MaritalStatus | nvarchar(1) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Gender | nvarchar(1) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| BirthDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| PartnerName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| PartnerPhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| ChildrenCount | int | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| HomePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| EMail2 | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsMember | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsJoker | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsNotCallMe | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsLogo | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| ContactChannel | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Source | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Category | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| OfficePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| OfficeAddress | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| ReferanceUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| LogoID | int | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Password | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| TaxNo | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CustomerTaxNo | varchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| TaxOffice | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsInAutomation | bit | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| LastMoveMesken | bit | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| HasComplaint | bit | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| LastTalkDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| Param01 | bit | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CanPayByVP | bit | Hayir | ((1)) | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| NationalityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| CustomerType | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| FatherName | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| MotherName | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| BirthPlace | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| VerificationMethod | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| NaceCode | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IsMFAEnabled | bit | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IdentitySerialNumber | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |
| IdentityExpirationDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Advices; Crm.AppointmentAssignments; Crm.Complaints; Crm.CustomerLogins; Crm.Customers; Crm.DataAnalysisLogs; Crm.ETesisTerkinIntegrations; Crm.Files; Crm.InternetSubeLogs; Crm.OffsetLogs; Crm.Opportunities; Crm.Organizations; Crm.Portfolios; Crm.SetOffLogs; Crm.Simulations; Crm.SmsLogs; Crm.Users |  |

## Crm.CustomerSources

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsLeadRequired | bit | Hayir | ((0)) | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsBranch | bit | Hayir | ((1)) | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsMarketing | bit | Hayir | ((0)) | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| UtmSources | nvarchar(200) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsDigital | bit | Hayir | ((0)) | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsActive | bit | Hayir | ((1)) | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |
| IysSource | nvarchar(100) | Evet |  | Hayir |  | Crm.CampaignSources; Crm.Opportunities; Crm.Users |  |

## Crm.DailyServicePricePaidLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| InstallmentUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| ProcessDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(5) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.DataAnalysisLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Users |  |
| Code | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |
| IsConfirmed | bit | Evet | ((0)) | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Users |  |

## Crm.Debits

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.InventoryDebits; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.InventoryDebits; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.InventoryDebits; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.InventoryDebits; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.InventoryDebits; Crm.Users |  |
| DebitFile | nvarchar(100) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| Status | nvarchar(100) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| Note | nvarchar(1000) | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| InventoryUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.InventoryDebits; Crm.Users |  |

## Crm.Deliveries

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| CostInclusive | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| AssurancePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| ExpertizePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| DeliveryAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| DeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| FinancialDeliveryDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| PaperWorkCompleteDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| OffsettingContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| ProductType | nvarchar(max) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| IsComplete | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |
| Receipt | varchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgageTypes; Crm.Users |  |

## Crm.DeliveryCallHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.DeliveryCalls; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| DeliveryCallUid | uniqueidentifier | Hayir |  | Hayir | Crm.DeliveryCalls.Uid | Crm.DeliveryCalls; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| OutBoundCallUid | uniqueidentifier | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CallCount | int | Hayir | ((0)) | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| Status | smallint | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| RecallDate | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| UnReachedDate | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| OldValue | nvarchar(max) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| NewValue | nvarchar(max) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| TransactionName | nvarchar(100) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| OldValueText | nvarchar(100) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| NewValueText | nvarchar(100) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| FieldNameText | nvarchar(100) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| DocumentRequestedDate | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |

## Crm.DeliveryCallNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.DeliveryCalls; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryCalls; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| DeliveryCallUid | uniqueidentifier | Hayir |  | Hayir | Crm.DeliveryCalls.Uid | Crm.DeliveryCalls; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| NoteText | nvarchar(max) | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.DeliveryCalls; Crm.Users |  |

## Crm.DeliveryCalls

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| OutBoundCallUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| CallCount | int | Hayir | ((0)) | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| Status | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| RecallDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| UnReachedDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |
| DocumentRequestedDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.Users |  |

## Crm.DeliveryDocumentApprovals

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| FileTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.FileTypes.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| OldStatus | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| Comment | nvarchar(max) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| IsRequired | bit | Hayir | ((1)) | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| ProductType | nvarchar(2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| ControlAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| ControlBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| SendApprovalBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |
| GuarontorName | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files |  |

## Crm.DeliveryEmployees

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Users |  |
| DayOfWeek | int | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |

## Crm.DeliveryFiles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| DeliveryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| FileTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.FileTypes.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| GuarantorUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |
| Status | varchar(2) | Evet |  | Hayir |  | Crm.Contracts; Crm.FileTypes; Crm.Files; Crm.Users |  |

## Crm.DeliveryPaymentLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| LogType | smallint | Evet |  | Hayir |  |  |  |
| Department | nvarchar(100) | Evet |  | Hayir |  |  |  |
| DeliveryPaymentUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |  |

## Crm.DeliveryPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.MortgageTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgageTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgageTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgageTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid | Crm.MortgageTypes; Crm.Users |  |
| DeliveryAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| ProductType | nvarchar(10) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| InsuranceDeduction | decimal(18,2) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| CompletedDeliveryAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| BeforeDeliveryStatus | nvarchar(50) | Hayir |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| BeforeDeliverySubStatus | smallint | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| DeliveryRefundLogoManualAction | bit | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| RefundAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| DeliveryApprovalDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| DeliveryRefundDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| LogoNo | bigint | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| LogoProcessDate | datetime | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| BankUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| BankAccountUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| Status | smallint | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| Message | varchar(max) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| AccountList | varchar(max) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| ErrorList | varchar(max) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| DeliveryApporovalUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgageTypes; Crm.Users |  |
| Notes | varchar(max) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |
| PaymentUserUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgageTypes; Crm.Users |  |

## Crm.DeliveryRanges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid | Crm.Products; Crm.Users |  |
| StartMonth | int | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| EndMonth | int | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| StartMonthNotCampaign | int | Hayir | ((0)) | Hayir |  | Crm.Products; Crm.Users |  |
| EndMonthNotCampaign | int | Hayir | ((0)) | Hayir |  | Crm.Products; Crm.Users |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |

## Crm.DeliveryWorkAdvances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |
| EndingAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.DeprivationInqueries

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| PlateNumber | nvarchar(50) | Evet |  | Hayir |  |  |  |
| RegistrationSerialNumber | nvarchar(50) | Evet |  | Hayir |  |  |  |
| AsbisRegistrationReferenceNumber | nvarchar(50) | Evet |  | Hayir |  |  |  |
| VehicleType | int | Evet |  | Hayir |  |  |  |
| VehicleBrand | nvarchar(50) | Evet |  | Hayir |  |  |  |
| Year | int | Evet |  | Hayir |  |  |  |
| RegistrationStatus | bit | Hayir |  | Hayir |  |  |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| ReasonType | smallint | Evet |  | Hayir |  |  |  |

## Crm.Distraints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| DistraintOffice | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| FileNumber | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| RenewalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Files; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.Users |  |

## Crm.DocumentReads

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| DocumentUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| AllOrganitionRead | bit | Hayir | ((0)) | Hayir |  |  |  |
| AllRegionsRead | bit | Hayir | ((0)) | Hayir |  |  |  |

## Crm.Documents

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| ImportUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| Order | int | Hayir |  | Hayir |  | Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |

## Crm.DrawCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| DrawUid | uniqueidentifier | Evet |  | Hayir | Crm.Draws.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Activities; Crm.Contracts; Crm.Draws; Crm.Users |  |

## Crm.Draws

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| Message | nvarchar(4000) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| CodeLength | int | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| IsAppointment | bit | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| AppointmentCodeCount | int | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| IsContract | bit | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| ContractCodeCount | int | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| IsCandidate | bit | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| CandidateCodeCount | int | Hayir |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| CodeMessage | nvarchar(4000) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |
| ContractMessage | nvarchar(4000) | Evet |  | Hayir |  | Crm.DrawCodes; Crm.Organizations; Crm.Users |  |

## Crm.ETesisTerkinContractIbans

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| ETesisTerkinIntegrationUid | uniqueidentifier | Hayir |  | Hayir | Crm.ETesisTerkinIntegrations.Uid | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |
| ContractIBANUid | uniqueidentifier | Hayir |  | Hayir | Crm.ContractIBANs.Uid | Crm.ContractIBANs; Crm.ETesisTerkinIntegrations; Crm.Users |  |

## Crm.ETesisTerkinIntegrations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| MortgageUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| IntegrationNo | nvarchar(450) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Customers.Uid | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| InsuranceUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ImmovableCityId | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ImmovableTownId | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ImmovableHomeTownId | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ImmovableBlock | nvarchar(255) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| ImmovableParcel | nvarchar(255) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| IndependentUnitNo | nvarchar(255) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| LandOffice | nvarchar(255) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| DocumentNumber | nvarchar(255) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| LandOfficeId | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| WageDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| WageNumber | varchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| Type | smallint | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| MortgagePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| MortgageFileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| OfficialDeedFileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |
| CancelDescription | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.ETesisTerkinContractIbans; Crm.Users |  |

## Crm.Files

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Link | nvarchar(100) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DistraintUid | uniqueidentifier | Evet |  | Hayir | Crm.Distraints.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| InventoryUid | uniqueidentifier | Evet |  | Hayir | Crm.Inventories.Uid | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| FileTypeUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DeliveryHistoryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Status | varchar(2) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DeliveryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| GuarantorUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| DeliveryFileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| CandidateUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| MortgageInsuranceUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| TransferStatus | smallint | Evet | ((0)) | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| ApproveAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| RejectAt | datetime2(7) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| RejectUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Path | nvarchar(400) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| ComplaintUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| ComplaintNoteUid | uniqueidentifier | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| TicketUid | nvarchar(100) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Hash | varchar(400) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| AuthorizationId | varchar(400) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |
| Fingerprint | nvarchar(400) | Evet |  | Hayir |  | Crm.ContractRevisions; Crm.Contracts; Crm.Customers; Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Distraints; Crm.Inventories; Crm.Mortgages; Crm.Users |  |

## Crm.FileTypeCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Key | nvarchar(4) | Evet |  | Hayir |  | Crm.Users |  |
| OrderBy | int | Evet |  | Hayir |  | Crm.Users |  |

## Crm.FileTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| Name | nvarchar(max) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| Type | nvarchar(4) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| IsRequired | bit | Hayir |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| Department | nvarchar(4) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| OrderBy | int | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| IsTradesman | bit | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| IsGuarantor | bit | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| IsDelivery | bit | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| ProductType | nvarchar(2) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| CategoryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| IsLegalProceeding | bit | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| Path | varchar(300) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| NewPath | varchar(300) | Evet |  | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |
| TransferStatus | smallint | Hayir | ((0)) | Hayir |  | Crm.DeliveryDocumentApprovals; Crm.DeliveryFiles; Crm.Users |  |

## Crm.Firms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DefaultGroupStartDay | int | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |

## Crm.GroupProducts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Groups; Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Groups; Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Groups; Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Groups; Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Groups; Crm.Products; Crm.Users |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.Groups.Uid | Crm.Groups; Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid | Crm.Groups; Crm.Products; Crm.Users |  |

## Crm.Groups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| GroupDate | datetime2(7) | Hayir |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| IsOpen | bit | Hayir |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| ClosedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| InstallmentCount | int | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| LimitedProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |
| IsPool | bit | Hayir | ((0)) | Hayir |  | Crm.GroupProducts; Crm.NotaryResults; Crm.Users |  |

## Crm.GroupsForBulkDrawQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| NotaryName | nvarchar(400) | Hayir |  | Hayir |  |  |  |
| OrganizationPlace | nvarchar(1000) | Hayir |  | Hayir |  |  |  |
| OrganizationDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Status | smallint | Evet |  | Hayir |  |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |  |
| BallCount | int | Hayir | ((0)) | Hayir |  |  |  |
| Message | nvarchar(1000) | Evet |  | Hayir |  |  |  |

## Crm.Guarantors

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Tckno | nvarchar(20) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Phone | nvarchar(20) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Address | nvarchar(500) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Users |  |
| Number | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| IsTradesman | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |

## Crm.Holidays

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Evet |  | Hayir |  |  |  |
| Name | varchar(50) | Evet |  | Hayir |  |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| Year | int | Evet |  | Hayir |  |  |  |
| Total | decimal(18,2) | Evet |  | Hayir |  |  |  |

## Crm.Installments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.PremiumItems |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.PremiumItems |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.PremiumItems |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.PremiumItems |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| ContractRevisionUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| InstallmentNumber | int | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| Status | nvarchar(100) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| PricePaid | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| DueDate | datetime2(7) | Hayir |  | Hayir |  | Crm.PremiumItems |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| VariableIndexUid | uniqueidentifier | Evet |  | Hayir |  | Crm.PremiumItems |  |
| IsLogo | bit | Hayir | ((0)) | Hayir |  | Crm.PremiumItems |  |
| IsLast | bit | Hayir | ((0)) | Hayir |  | Crm.PremiumItems |  |
| SentCountSMS | int | Hayir | ((0)) | Hayir |  | Crm.PremiumItems |  |
| PostponePrice | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.PremiumItems |  |
| PostponePricePaid | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.PremiumItems |  |
| BankLogUid | uniqueidentifier | Evet |  | Hayir |  | Crm.PremiumItems |  |
| DidBillSend | bit | Evet |  | Hayir |  | Crm.PremiumItems |  |
| ProcessDate | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.PremiumItems |  |
| Sub_Type | nvarchar(10) | Evet |  | Hayir |  | Crm.PremiumItems |  |
| Sub_InstallmentNumber | int | Evet |  | Hayir |  | Crm.PremiumItems |  |
| PromissoryNotePostingDate | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumItems |  |

## Crm.IntegrationApiLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| JsonData | nvarchar(1000) | Evet |  | Hayir |  | Crm.Users |  |
| Result | nvarchar(2500) | Evet |  | Hayir |  | Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.IntegrationApiLogs250919

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| JsonData | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| Result | nvarchar(2000) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.InternalFiles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir | (getdate()) | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Link | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| InternalFileTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| RejectUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |  |

## Crm.InternalFileTypeCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Key | nvarchar(5) | Evet |  | Hayir |  |  |  |

## Crm.InternalFileTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Name | nvarchar(max) | Evet |  | Hayir |  |  |  |
| Type | nvarchar(4) | Evet |  | Hayir |  |  |  |
| IsRequired | bit | Hayir |  | Hayir |  |  |  |
| Department | nvarchar(4) | Evet |  | Hayir |  |  |  |
| OrderBy | int | Evet |  | Hayir |  |  |  |
| ProductType | nvarchar(2) | Evet |  | Hayir |  |  |  |
| CategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Path | varchar(250) | Evet |  | Hayir |  |  |  |

## Crm.InternetSubeLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.Users |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |

## Crm.Inventories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Code | bigint | Hayir |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users | Identity |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| InventoryTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.InventoryTypes.Uid | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| DateOfPurchase | datetime2(7) | Hayir |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| BuyCompany | nvarchar(1000) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| InvoiceFile | nvarchar(1000) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Brand | nvarchar(1000) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Model | nvarchar(500) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| SerialNumber | nvarchar(400) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| Json | nvarchar(4000) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |
| AssetTag | nvarchar(50) | Evet |  | Hayir |  | Crm.Files; Crm.InventoryDebits; Crm.InventoryTypes; Crm.Users |  |

## Crm.InventoryDebits

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Debits; Crm.Inventories; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Debits; Crm.Inventories; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Debits; Crm.Inventories; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Debits; Crm.Inventories; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Debits; Crm.Inventories; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Debits; Crm.Inventories; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Debits; Crm.Inventories; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Debits; Crm.Inventories; Crm.Users |  |
| DebitUid | uniqueidentifier | Evet |  | Hayir | Crm.Debits.Uid | Crm.Debits; Crm.Inventories; Crm.Users |  |
| InventoryUid | uniqueidentifier | Evet |  | Hayir | Crm.Inventories.Uid | Crm.Debits; Crm.Inventories; Crm.Users |  |

## Crm.InventoryTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Inventories; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Inventories; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Inventories; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Inventories; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Inventories; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Inventories; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Inventories; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Inventories; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Inventories; Crm.Users |  |
| Properties | nvarchar(500) | Evet |  | Hayir |  | Crm.Inventories; Crm.Users |  |

## Crm.InvoiceLogoLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Users |  |
| CustomerNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| ContractNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InvoiceRef | nvarchar(200) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InvoiceAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| BsmvAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| BsmvRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| InvoiceNo | varchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| BsmvCode | varchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Status | smallint | Hayir | ((0)) | Hayir |  | Crm.Contracts; Crm.Users |  |
| InvoiceServiceCode | varchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |
| Message | varchar(max) | Evet |  | Hayir |  | Crm.Contracts; Crm.Users |  |

## Crm.IssueHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| DirectUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| DirectDescription | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Subject | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Explanation | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| IsAnswer | bit | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Answer | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| AnswerBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| Status | nvarchar(max) | Evet |  | Hayir |  | Crm.Issues; Crm.Organizations; Crm.Users |  |
| IssueUid | uniqueidentifier | Evet |  | Hayir | Crm.Issues.Uid | Crm.Issues; Crm.Organizations; Crm.Users |  |

## Crm.Issues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Code | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| DirectUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| DirectDescription | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Subject | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Explanation | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| IsAnswer | bit | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Answer | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| AnswerBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |
| Status | nvarchar(max) | Evet |  | Hayir |  | Crm.IssueHistories; Crm.Organizations; Crm.Users |  |

## Crm.ITSystemUserLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  |  |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| IsLdap | bit | Evet |  | Hayir |  |  |  |

## Crm.LeadForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| ID | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| FormID | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| FormCreateDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| CampaignID | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| AdID | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| AdSetID | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Platform | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Log | nvarchar(max) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| RecordType | nvarchar(1) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| InstallmentRange | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| PriceRange | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| FormUid | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| Note | nvarchar(4000) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| AdFormUid | uniqueidentifier | Evet |  | Hayir | Crm.AdForms.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| IsRecurring | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| IsRecurringOld | bit | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| IsDigitalRecurring | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |
| MobilePhone2 | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.AdForms; Crm.Organizations; Crm.Users |  |

## Crm.Leads

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Message | nvarchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Status | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Source | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsContact | bit | Evet | ((1)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| EMail | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CancellationReason | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| WaitDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MemberDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CampaignUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CampaignItemUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MaritalStatus | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Gender | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ReferanceUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertToCandidateDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertToCandidateByUserUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsCenter | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CallOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsAppointmentConvert | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertType | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsHomeCar | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsHomeCarManuel | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsDontCall | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsDontSms | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MobilePhone2 | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MobilePhoneFormat | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OwnerBrandEnvoyUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OwnerBrandEnvoyPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| BrandEnvoyDate | datetime | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| BrandEnvoyCall | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| BrandEnvoyCallOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| BrandEnvoyCallDate | datetime | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CountOfCallLead | int | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CountOfCallCandidate | int | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CreatedByUserOrganizationType | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioRegionUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsAppointment | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsPendingActivity | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| LastContactDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsRecentlyPassive | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CountryName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CityName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| TownName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| HomeTownName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioCode | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| PortfolioOrganizationName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OccupationName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerSourceName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CreatedByUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| UpdatedByUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertToCandidateByUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CallOwnerName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerSourceIsDigital | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerSourceIsMarketing | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CustomerBirthDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsJoinJob | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| RepPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsDuplicateBrandEnvoyLead | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| LastTalkDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| OwnerRepFamiliarity | nvarchar(5) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsInAutomation | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| SmsChaseDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| MeskenCustomerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| AutomationListName | varchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IysTransactionId | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IysRequestId | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IysSubRequestId | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| SaveAgainDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Tckno | varchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| TaxNo | varchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| TmsfFirmId | smallint | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| Address | varchar(200) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| TMSFFirmIds | varchar(20) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| AutoPortfolioAssignment | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| FULLNAME | computed |  |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes | Computed |
| HardDeleted | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CancellationedByUserName | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CancellationedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CancellationedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsDontEmail | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertToCancelByManuel | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConvertToCandidateByManuel | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsRecurring | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CallCenterContactKey | varchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsSmsVerified | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| CallCenterContactUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsClarification | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ClarificationDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConsentIp | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConsentVersion | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| IsConsent | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ConsentDate | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ClarificationIp | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |
| ClarificationVersion | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Opportunities; Crm.SmsLogs; Crm.SmsVerificationCodes |  |

## Crm.LoginFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| MachineName | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Message | nvarchar(400) | Evet |  | Hayir |  | Crm.Users |  |
| IsLdap | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Device | nvarchar(20) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.Logins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| IP | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Host | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| IsCrm | bit | Evet |  | Hayir |  | Crm.Users |  |
| IsLdap | bit | Evet |  | Hayir |  | Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |

## Crm.LogoLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| LOGICALREF | int | Hayir |  | Hayir |  | Crm.Users |  |
| LINEEXP | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| TRANNO | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| ACCFICHEREF | int | Hayir |  | Hayir |  | Crm.Users |  |
| GENEXP1 | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| AMOUNT | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| CODE | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| CAPIBLOCK_CREADEDDATE | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CAPIBLOCK_MODIFIEDDATE | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| TYPE | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| PAYMENT_DATE | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.LogoPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| LogicalRef | int | Hayir |  | Hayir |  | Crm.Users |  |
| LineExp | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| TranNo | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| AccfichefRef | int | Hayir |  | Hayir |  | Crm.Users |  |
| GenexP1 | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| Code | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| CapiBlock_CreatedDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CapiBlock_ModifiedDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| PaymentDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| Message | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |

## Crm.LogoServiceLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| PostData | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| GetData | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| ServiceUrl | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| IsSuccess | bit | Hayir |  | Hayir |  | Crm.Users |  |

## Crm.ManuelLeadForCallCenterQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| LeadUid | varchar(50) | Hayir |  | Hayir |  | Crm.Users |  |
| Name | varchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| SurName | varchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Email | varchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| MobilePhone | varchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| CampaignId | varchar(300) | Evet |  | Hayir |  | Crm.Users |  |
| ManuelListName | varchar(300) | Evet |  | Hayir |  | Crm.Users |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| Message | varchar(300) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.ManuelPaymentRequests

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(10) | Hayir |  | Hayir |  |  |  |
| Status | nvarchar(10) | Hayir |  | Hayir |  |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| ContractStatus  | nvarchar(10) | Evet |  | Hayir |  |  |  |
| TotalPaymentBeforeRequest | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| Description | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Year | int | Hayir |  | Hayir |  |  |  |
| Month | int | Hayir |  | Hayir |  |  |  |
| ParentRegionUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| BranchUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| RejectedUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| RejectedDate | datetime2(7) | Evet |  | Hayir |  |  |  |

## Crm.MobileApplicationConfigurations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Appkey | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| Value | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| Platform | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| ID | int | Hayir |  | Hayir |  | Crm.Users |  |
| Description | nvarchar(400) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.MobileConfigurationSettings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| AppId | int | Hayir |  | Hayir |  | Crm.Users |  |
| PlatformId | int | Hayir |  | Hayir |  | Crm.Users |  |
| VersionNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| DownloadLink | nvarchar(250) | Evet |  | Hayir |  | Crm.Users |  |
| WarningMessage | nvarchar(500) | Evet |  | Hayir |  | Crm.Users |  |
| IsNative | bit | Hayir |  | Hayir |  | Crm.Users |  |
| ForceUpdate | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Enabled | bit | Hayir |  | Hayir |  | Crm.Users |  |
| ServiceUrl | nvarchar(250) | Evet |  | Hayir |  | Crm.Users |  |
| StoreStatus | int | Evet |  | Hayir |  | Crm.Users |  |

## Crm.MobilePhoneNumbers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Number | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |

## Crm.ModuleAuths

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.Modules; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.Modules; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.Modules; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| Name | nvarchar(200) | Evet |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.Authorities; Crm.Modules; Crm.Users |  |
| ModuleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Modules.Uid | Crm.Authorities; Crm.Modules; Crm.Users |  |

## Crm.Modules

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.ModuleAuths; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.ModuleAuths; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |
| Name | nvarchar(200) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.ModuleAuths; Crm.Users |  |

## Crm.MortgageCosts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Mortgages; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid | Crm.Mortgages; Crm.Users |  |
| Description | varchar(250) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Month | int | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Year | int | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |

## Crm.MortgageInsurances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Mortgages; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| FinalAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Type | smallint | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| Description | nvarchar(max) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid | Crm.Mortgages; Crm.Users |  |
| DidConsensusDone | bit | Evet | ((0)) | Hayir |  | Crm.Mortgages; Crm.Users |  |
| InsurancePaymentMethod | nvarchar(50) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| RenewalsNumber | int | Hayir | ((0)) | Hayir |  | Crm.Mortgages; Crm.Users |  |
| IsRenewed | bit | Hayir | ((0)) | Hayir |  | Crm.Mortgages; Crm.Users |  |
| PolicyStartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| PolicyEndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| IsTraceable | bit | Hayir | ((1)) | Hayir |  | Crm.Mortgages; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| PreviousInsuranceUID | uniqueidentifier | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| InsurancePlace | smallint | Hayir | ((0)) | Hayir |  | Crm.Mortgages; Crm.Users |  |
| PolicyNo | nvarchar(255) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| BuildingCollateralAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| PolicyCompanyUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |

## Crm.MortgageLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Mortgages; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Mortgages; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| MortgageState | nvarchar(4000) | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |
| MortgageUid | uniqueidentifier | Hayir |  | Hayir | Crm.Mortgages.Uid | Crm.Mortgages; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Mortgages; Crm.Users |  |

## Crm.MortgagePledgeConsents

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| PledgeUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |  |
| TCKN | varchar(50) | Evet |  | Hayir |  |  |  |
| TaxNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| VehiclePlateNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  |  |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| EndDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |  |
| ConsentEGMRReferenceNo | bigint | Evet |  | Hayir |  |  |  |
| Description | varchar(400) | Evet |  | Hayir |  |  |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |  |
| Process | smallint | Hayir |  | Hayir |  |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |  |

## Crm.MortgagePledgeRemovals

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| PledgeUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |  |
| RemovalRequestDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |  |
| RemovalReason | smallint | Evet |  | Hayir |  |  |  |

## Crm.MortgagePledges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehiclePlateNumber | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehicleRegistrationSerialNumber | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehicleAsbisRegistrationReferenceNumber | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| DocumentID | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| PledgeRequestDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| BankName | varchar(150) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| BankBranchCode | int | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehicleRegistrationID | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehicleType | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| VehicleProblemStatus | int | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| TNBInsertSequence | int | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| TNBInsertDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| QueueStatus | smallint | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |
| PledgeRemovalUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePrePledges; Crm.SustainabilityReports |  |

## Crm.MortgagePledgeVehicleBrandModels

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| Name | nvarchar(100) | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |
| MortgagePledgeVehicleBrandUid | uniqueidentifier | Hayir |  | Hayir | Crm.MortgagePledgeVehicleBrands.Uid | Crm.MortgagePledgeVehicleBrands; Crm.Users |  |

## Crm.MortgagePledgeVehicleBrands

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.MortgagePledgeVehicleBrandModels |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |
| Name | varchar(50) | Hayir |  | Hayir |  | Crm.MortgagePledgeVehicleBrandModels |  |

## Crm.MortgagePledgeVehicleTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ID | int | Hayir |  | Hayir |  |  |  |
| Name | varchar(50) | Hayir |  | Hayir |  |  |  |
| Order | int | Hayir |  | Hayir |  |  | Identity |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |  |

## Crm.MortgagePrePledges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.MortgagePledges |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.MortgagePledges |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.MortgagePledges |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.MortgagePledges |  |
| Name | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| Surname | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| TCKN | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| ModelYear | varchar(50) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| VehicleType | int | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| VehicleBrand | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| PrePledgeRequestDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| BankName | varchar(150) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| BankBranchCode | int | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| TNBEGMRReferenceNo | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| VehicleRegistrationSerialNumber | varchar(100) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| TNBInsertDate | datetime2(7) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueStatus | smallint | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueStatusConvertPledge | smallint | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueSubStatusConvertPledge | smallint | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| QueueMessageConvertPledge | varchar(max) | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| MortgagePledgeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgagePledges.Uid | Crm.MortgagePledges |  |
| VehicleBrandUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| VehicleModelUid | uniqueidentifier | Evet |  | Hayir |  | Crm.MortgagePledges |  |
| TaxNo | nvarchar(10) | Evet |  | Hayir |  | Crm.MortgagePledges |  |

## Crm.Mortgages

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Status | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| MortgageOffice | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| FileNumber | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| RenewalDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Price | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| IsPricePaid | bit | Hayir | ((0)) | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| NotaryOffice | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| WageNumber | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| PledgeDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| PricePaid | decimal(18,0) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| LandOffice | nvarchar(100) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| AmountOfBidBond | decimal(18,0) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ReleaseDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| LegalStatus | varchar(25) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ClosedDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| SubTypeUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ActiveDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Files; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |

## Crm.MortgageTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Key | nvarchar(100) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Fields | nvarchar(3000) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Formula | nvarchar(200) | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| IsPrivileged | bit | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| canBeRenewed | bit | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| ParentTypeUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |
| Order | smallint | Evet |  | Hayir |  | Crm.Deliveries; Crm.DeliveryPayments; Crm.Mortgages; Crm.SustainabilityReports; Crm.Users |  |

## Crm.NaceCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| NaceCode | nvarchar(10) | Hayir |  | Hayir |  |  |  |
| SectorCode | nvarchar(10) | Evet |  | Hayir |  |  |  |
| SectorDefinition | nvarchar(100) | Evet |  | Hayir |  |  |  |
| OccupationCode | nvarchar(10) | Evet |  | Hayir |  |  |  |
| OccupationDefinition | nvarchar(255) | Evet |  | Hayir |  |  |  |
| NaceDescription | nvarchar(4000) | Evet |  | Hayir |  |  |  |

## Crm.Nationalities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Code | nvarchar(20) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.NotaryLists

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| NotaryResultUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotaryResults.Uid | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| Month | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| IsSuccess | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |
| DrawOrderNo | int | Hayir | ((0)) | Hayir |  | Crm.Contracts; Crm.NotaryResults; Crm.Users |  |

## Crm.NotaryResults

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.Groups.Uid | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| NotaryName | nvarchar(100) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| OrganizationDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| OrganizationPlace | nvarchar(100) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| NotaryFile | nvarchar(200) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| MinMonth | int | Hayir |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| ApproveControllerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| ApproveControllerDate | datetime2(7) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| OldNotaryFile | nvarchar(200) | Evet |  | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  | Crm.Groups; Crm.NotaryLists; Crm.Users |  |

## Crm.NotDeliveredOnDeliveryDates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| FinanceDeliveryDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| ProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |  |
| ProductPriceWithInsuranceCuts | decimal(18,2) | Evet |  | Hayir |  |  |  |

## Crm.NotificationGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Name | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Key | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Description | nvarchar(150) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Message | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Token | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| LastSendingDate | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| TotalSendingCount | int | Hayir |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| LastSenderUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| Title | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |
| ProcedureName | varchar(50) | Evet |  | Hayir |  | Crm.NotificationGroupSubscriber; Crm.NotificationLogs; Crm.Users |  |

## Crm.NotificationGroupSubscriber

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotificationGroups.Uid | Crm.NotificationGroups; Crm.Reps; Crm.Users |  |

## Crm.NotificationLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.NotificationGroups; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.NotificationGroups; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| NotificationGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotificationGroups.Uid | Crm.NotificationGroups; Crm.Users |  |
| Title | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| Message | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| ImageUrl | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| Data | nvarchar(max) | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  | Crm.NotificationGroups; Crm.Users |  |

## Crm.NotificationVariables

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Key | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.Occupations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Opportunities; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Opportunities; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Opportunities; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Opportunities; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Opportunities; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Opportunities; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Opportunities; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Opportunities; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Opportunities; Crm.Users |  |

## Crm.OffsetLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OrganizationName | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| RegionName | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PetitionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| TransactionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PortfolioOwnerName | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.Users |  |
| OffsetContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetContractNo | nvarchar(max) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractNo | nvarchar(10) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetProductName | nvarchar(150) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewProductName | nvarchar(150) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetContractCreatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractCreatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetIsDraw | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewIsDraw | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| IncrementRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewGroupName | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetServiceType | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewServiceType | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetRawServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Status | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Description | nvarchar(500) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CustomerName | nvarchar(150) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetGroupName | nvarchar(max) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Year | int | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Month | int | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetInstallmentCount | nvarchar(3) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewInstallmentCount | nvarchar(3) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| ProductPriceDifference | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| ServicePriceDifference | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractStatus | nvarchar(3) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewPaidServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetPaidServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewTotalPaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetTotalPaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewServicePriceReflected | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| BidApprovalRole | varchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| SubStatus | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CompletedPriceDifference | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OffsetContractServiceRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractServiceRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| IsContractRevisionDecrease | bit | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |

## Crm.OffsetProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| OffsetLogUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Department | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |  |
| OffsetProcessType | smallint | Hayir |  | Hayir |  |  |  |

## Crm.OnlineUsers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Token | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| ComputerName | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| Device | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| SysStartTime | datetime2(7) | Hayir | (sysutcdatetime()) | Hayir |  | Crm.Users |  |
| SysEndTime | datetime2(7) | Hayir | (CONVERT([datetime2],'9999-12-31 23:59:59.9999999')) | Hayir |  | Crm.Users |  |

## Crm.Opportunities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MinProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MaxProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MinCashPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MaxCashPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MinServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MaxServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| InComeLevelOfMonth | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MinMontlyAffordAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| MaxMontlyAffordAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| RentPriceOfMonth | decimal(18,2) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| IsTenant | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| IsInterimPayment | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| IsIncreasedInstallement | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| IsServicePriceInstallement | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| LeadUid | uniqueidentifier | Hayir |  | Hayir | Crm.Leads.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| Temperature | int | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir | Crm.CustomerSources.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| CustomerUid1 | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir | Crm.Occupations.Uid | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.Areas; Crm.CustomerSources; Crm.Customers; Crm.Leads; Crm.Occupations; Crm.Portfolios; Crm.SmsLogs; Crm.Users |  |

## Crm.OrganizationAreas

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Areas; Crm.Organizations; Crm.Users |  |
| AreaUid | uniqueidentifier | Hayir |  | Hayir | Crm.Areas.Uid | Crm.Areas; Crm.Organizations; Crm.Users |  |
| LastAssignment | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.Organizations; Crm.Users |  |

## Crm.OrganizationHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |

## Crm.OrganizationMonthlyTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| Period | datetime | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Users |  |
| Target | bigint | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |

## Crm.Organizations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| FirmUid | uniqueidentifier | Evet |  | Hayir | Crm.Firms.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Address | nvarchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| MuhasebeCode | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| AddressDescription | nvarchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| MapLink | nvarchar(200) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| PhotoLink | nvarchar(200) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CostCode | nvarchar(100) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| LeadCount | int | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| OldLeadCount | int | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| BranchCategoryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| ManagerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| BankCode | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Gl_Code349 | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Gl_Code136 | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| NameForLogo | varchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| CostCodeForLogo | varchar(4) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| IsPassive | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| MonthlyBudgetAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| ADOrganizationalUnit | varchar(200) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| EnabledLdap | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| EnabledKEPLastVersion | bit | Hayir | ((0)) | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| BranchID | int | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| AppleMapsLink | nvarchar(200) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| IsUsedForFeedback | bit | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |
| Email | nvarchar(50) | Evet |  | Hayir |  | Crm.AppointmentAssignments; Crm.Areas; Crm.BankDetails; Crm.CampaignBranches; Crm.Costs; Crm.Customers; Crm.DeliveryEmployees; Crm.Draws; Crm.Firms; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Portfolios; Crm.PosPayments; Crm.Premiums; Crm.Reps; Crm.RiskTrackings; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.Users |  |

## Crm.Performances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| PerformanceDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| Point | int | Hayir |  | Hayir |  | Crm.Users |  |
| PhonePoint | int | Hayir |  | Hayir |  | Crm.Users |  |
| AppointmentCount | int | Hayir |  | Hayir |  | Crm.Users |  |
| AppointmentPoint | int | Hayir |  | Hayir |  | Crm.Users |  |
| OutAppointmentCount | int | Hayir |  | Hayir |  | Crm.Users |  |
| OutAppointmentPoint | int | Hayir |  | Hayir |  | Crm.Users |  |
| ContractCount | int | Hayir |  | Hayir |  | Crm.Users |  |
| ContractPoint | int | Hayir |  | Hayir |  | Crm.Users |  |
| PhoneCount | int | Hayir |  | Hayir |  | Crm.Users |  |

## Crm.PerformancesTemp

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| PerformanceDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| Point | int | Hayir |  | Hayir |  |  |  |
| PhonePoint | int | Hayir |  | Hayir |  |  |  |
| AppointmentCount | int | Hayir |  | Hayir |  |  |  |
| AppointmentPoint | int | Hayir |  | Hayir |  |  |  |
| OutAppointmentCount | int | Hayir |  | Hayir |  |  |  |
| OutAppointmentPoint | int | Hayir |  | Hayir |  |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |  |
| ContractPoint | int | Hayir |  | Hayir |  |  |  |
| PhoneCount | int | Hayir |  | Hayir |  |  |  |

## Crm.PlannedPeriodicDeliveryAmounts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Month | int | Evet |  | Hayir |  | Crm.Users |  |
| Year | int | Evet |  | Hayir |  | Crm.Users |  |
| PlannedAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |
| RealizedAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.Portfolios

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| Code | nvarchar(100) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| LastAssignDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| IsActive | bit | Evet | ((1)) | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| LastAssignBranchDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| LastAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| Type | varchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Opportunities; Crm.Organizations; Crm.Reps; Crm.UserHistories; Crm.UserPortfolios; Crm.Users |  |

## Crm.PosPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| LineNo | int | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| BankUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| IsTransferred | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |
| TransferDate | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Organizations; Crm.Users |  |

## Crm.PostVirmanQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| OldContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| OldCustomerUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| OldCustomerNo | nvarchar(450) | Hayir |  | Hayir |  | Crm.Users |  |
| NewContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| NewCustomerUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| NewCustomerNo | nvarchar(450) | Hayir |  | Hayir |  | Crm.Users |  |
| OldProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| NewProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| OldServicePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| NewServicePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| OldContractCreatedDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| NewContractCreatedDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| LogoProcessDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(10) | Evet |  | Hayir |  | Crm.Users |  |
| TotalPaid | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| RepPaymentPaid | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| JsonContent | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| Message | nvarchar(400) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.PremiumBranchRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.BranchCategories; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| BranchCategoryUid | uniqueidentifier | Hayir |  | Hayir | Crm.BranchCategories.Uid | Crm.BranchCategories; Crm.Users |  |
| Count | int | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| Target | decimal(18,2) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| ATarget | decimal(18,2) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| ARate | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.BranchCategories; Crm.Users |  |
| SalesmanRate | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.BranchCategories; Crm.Users |  |

## Crm.PremiumContracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| PremiumUid | uniqueidentifier | Evet |  | Hayir | Crm.Premiums.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| PremiumTimingUid | uniqueidentifier | Evet |  | Hayir | Crm.PremiumTimings.Uid | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| FirstMultiplier | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Factor | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Bonus | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Performance | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| DownPayment | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| PaymentInDays | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| PrimiumPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| BranchPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| IsInstallment | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.PremiumItems; Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |

## Crm.PremiumItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| PremiumUid | uniqueidentifier | Evet |  | Hayir | Crm.Premiums.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| PremiumContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumContracts.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| InstallmentUid | uniqueidentifier | Hayir |  | Hayir | Crm.Installments.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| InstallmentCount | int | Hayir |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| Type | int | Hayir |  | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| PrimiumPrice | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| Bonus | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| BranchPrice | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| PerformancePrice | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Installments; Crm.PremiumContracts; Crm.Premiums; Crm.Users |  |

## Crm.Premiums

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| Month | int | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| Year | int | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| BranchCategoryUid | uniqueidentifier | Hayir |  | Hayir | Crm.BranchCategories.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| CurrentPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| IsPaid | bit | Hayir |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| Rates | nvarchar(4000) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| PremiumTimingGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumTimingGroups.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| PaidDate | datetime2(7) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| PremiumUserTypeRateUid | uniqueidentifier | Evet |  | Hayir | Crm.PremiumUserTypeRates.Uid | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |
| TotalPremium | decimal(18,2) | Evet |  | Hayir |  | Crm.BranchCategories; Crm.Organizations; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumUserTypeRates; Crm.Roles; Crm.Users |  |

## Crm.PremiumTimingGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| IsNoneTiming | bit | Hayir |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumTimings; Crm.Premiums; Crm.Users |  |

## Crm.PremiumTimings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| PremiumTimingGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumTimingGroups.Uid | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| IsPaid | bit | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| ARate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| BRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| CRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| DRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| TRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| PaymentInDays | int | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| PaymentInDaysRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| PerformanceRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| DownPaymentRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| BranchTargetRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |
| BranchATargetRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.PremiumContracts; Crm.PremiumTimingGroups; Crm.Products; Crm.Users |  |

## Crm.PremiumUserTypeRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Premiums; Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Premiums; Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Premiums; Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.Premiums; Crm.Roles; Crm.Users |  |
| Percent | int | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| Scale | decimal(18,2) | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |
| Bonus | decimal(18,2) | Hayir |  | Hayir |  | Crm.Premiums; Crm.Roles; Crm.Users |  |

## Crm.Products

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| InstallmentCount | int | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Model | nvarchar(200) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DeliveryMonth | int | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashRateForBranch | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ContractHtml | nvarchar(500) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| FixedIndex | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.VariableIndexGroups.Uid | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IncreaseRateAfterDelivery | decimal(18,2) | Hayir |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchLast | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionLast | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDivided | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchFirst | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionFirst | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerFirst | decimal(18,2) | Evet | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDividedUntilDelivery | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceChargedBeforeDelivery | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDistributed | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedRateForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedRateForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignLast | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IncreaseRateAfterDeliveryArray | nvarchar(100) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MinProductPriceForDistributed | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MinProductPriceForDeliveryDistributed | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| PremiumRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| KayitVar | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| FlexibleDeliveryRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IncreaseRateBeforeDelivery | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| GroupLimit | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MaxProductPrice | decimal(18,0) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MinProductPrice | decimal(18,0) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DownPaymentUpperLimit | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceLoweLimit | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| FirstInstallmentRate | decimal(18,2) | Evet | ((1)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| Featured | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DistributedCashRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForCEO | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForCEOFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| PointServiceRateLimit | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashPaymentType | varchar(2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsCashPayment | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceInstallment | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceFirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentForGeneralManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceInstallmentCount | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCashPriceLimit | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| NoCashPaymentDiscount | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| AnnualRateOfIncrease | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| DiscountRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ElasticRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| InterimPayment | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MaxInstallmentCount | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MinDeliveryMonth | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| CashRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDividedFifth | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDividedFourth | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDividedSecond | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceDividedThird | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| PassiveDate | datetime2(7) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceChargedBeforeDeliveryRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDistributedRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceDividedUntilDeliveryRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignFirstFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignFirstFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignFirstThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignFirstTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignLastFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignLastFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignLastThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateDividedNotCampaignLastTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchFirstFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchFirstFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchFirstThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchFirstTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchLastFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchLastFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchLastThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchLastTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerFirstFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerFirstFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerFirstThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerFirstTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerLast | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerLastFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerLastFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerLastThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForBranchManagerLastTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerFirstFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerFirstFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerFirstThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerFirstTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerLastFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerLastFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerLastThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForGeneralManagerLastTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionFirstFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionFirstFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionFirstThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionFirstTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionLastFive | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionLastFour | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionLastThree | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServiceRateForRegionLastTwo | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| InflationRate | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsTmsf | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| OldProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| HasLottery | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| InstallmentPriceMaxLimit | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceCreditCardInstallment | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IncreaseRateByMonth | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| SixMonthsRateOfIncrease | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IncreasePeriodMonth | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| FirstServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| IsServicePriceCreditCardPartialInstallment | bit | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardPartialForBranch | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardPartialNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardPartialForRegion | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| ServicePriceCreditCardPartialForCEO | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| SpecialCashRateFirst | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| SpecialCashRateSecond | decimal(18,2) | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| FragmentationServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |
| PreventIncreaseAfterDelivery | bit | Hayir | ((0)) | Hayir |  | Crm.CashPriceIntervalRates; Crm.ContractTemplate; Crm.DeliveryRanges; Crm.GroupProducts; Crm.PremiumTimings; Crm.ServiceRateRanges; Crm.Users; Crm.VariableIndexGroups |  |

## Crm.ProxyOrganizations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ProxyUserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| ProxyStartDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| ProxyEndDate | datetime2(7) | Hayir |  | Hayir |  |  |  |

## Crm.QualityAnswers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| Point | int | Hayir |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| QualityQuestionUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityQuestions.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.QualityQuestions; Crm.Users |  |

## Crm.QualityForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityNotes; Crm.QualityQuestions; Crm.Users |  |

## Crm.QualityNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| Note | nvarchar(max) | Evet |  | Hayir |  | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid | Crm.Activities; Crm.QualityForms; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.QualityForms; Crm.Users |  |

## Crm.QualityQuestions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Type | nvarchar(100) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Order | int | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Weight | int | Hayir |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Question | nvarchar(4000) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.QualityAnswers; Crm.QualityForms; Crm.Users |  |

## Crm.RepCampaigns

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Reps |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Reps |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Reps |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Reps |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Reps |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Reps |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Reps |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Reps |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid | Crm.Reps |  |
| PeriodDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Reps |  |
| AdviceCount | int | Hayir |  | Hayir |  | Crm.Reps |  |
| DrawNumber | int | Evet |  | Hayir |  | Crm.Reps |  |
| Winner | smallint | Evet |  | Hayir |  | Crm.Reps |  |

## Crm.RepContracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid | Crm.Contracts; Crm.Reps; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Reps; Crm.Users |  |
| AllowanceYear | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |
| AllowanceMonth | int | Evet |  | Hayir |  | Crm.Contracts; Crm.Reps; Crm.Users |  |

## Crm.RepGifts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| ImagePath | nvarchar(500) | Evet |  | Hayir |  | Crm.Users |  |
| RequiredPoint | int | Hayir |  | Hayir |  | Crm.Users |  |

## Crm.RepIbans

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Reps; Crm.Users |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid | Crm.Reps; Crm.Users |  |
| Iban | nvarchar(50) | Evet |  | Hayir |  | Crm.Reps; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Reps; Crm.Users |  |
| BankCode | nvarchar(max) | Evet |  | Hayir |  | Crm.Reps; Crm.Users |  |

## Crm.RepPaymentDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| RepPaymentUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPayments.Uid | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| RepPointLogUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPointLogs.Uid | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |
| Point | int | Hayir | ((0)) | Hayir |  | Crm.RepPayments; Crm.RepPointLogs; Crm.Users |  |

## Crm.RepPaymentGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| GroupNo | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| TransferDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.RepPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| RepGiftUid | uniqueidentifier | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| TotalPoint | int | Hayir |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| TotalPaidAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| Status | nvarchar(50) | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| InstallmentUid | uniqueidentifier | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| RepPaymentGroupUid | uniqueidentifier | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |
| RepPaymentGroupNo | nvarchar(100) | Evet |  | Hayir |  | Crm.RepPaymentDetails; Crm.Reps; Crm.Users |  |

## Crm.RepPointLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| RepPointUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPoints.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| Point | int | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| CustomerLoginUid | uniqueidentifier | Evet |  | Hayir | Crm.CustomerLogins.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| IsPaid | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| IsProvision | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| PointPaid | int | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| InstallmentUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| AllowanceYear | int | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| AllowanceMonth | int | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |
| ContractPoint | int | Evet |  | Hayir |  | Crm.Activities; Crm.Contracts; Crm.CustomerLogins; Crm.RepPaymentDetails; Crm.RepPoints; Crm.Users |  |

## Crm.RepPoints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.RepPointLogs; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPointLogs; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPointLogs; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RepPointLogs; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| Point | int | Hayir |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| IsActive | bit | Hayir |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| DayLimit | int | Evet |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |
| Description | nvarchar(250) | Evet |  | Hayir |  | Crm.RepPointLogs; Crm.Users |  |

## Crm.Reps

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Surname | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| EMail | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Iban | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Tckno | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Address | nvarchar(2000) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsContract | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ContractText | nvarchar(max) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsBlock | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsRecommend | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir | Crm.Portfolios.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Reps.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Image | nvarchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| HasPaymentCard | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PushToken | nvarchar(200) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PendingPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OldPortfolioUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OwnerUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Code | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsLogo | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LogoID | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DailyAdviceCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DailyAdviceDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LastAnnouncementUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| BankCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IbanStatus | nvarchar(max) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| NotificationToken | nvarchar(max) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| NotificationId | nvarchar(max) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| BlockDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TotalPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ProvisionPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UsablePoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| AdviceCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LeadCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CandidateCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CancelledCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ContractCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ContractCancelledCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| AppointmentCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DontGoAppointmentCount | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioCode | varchar(10) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioName | varchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioOwner | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioOrganization | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| RegionManagerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UsedPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| RemainingPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| FutureDateNotPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ExpiredDateNotPoint | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DontGoAppointmentRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ContractCancelledRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UnreachableAdvice | int | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CandidateRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CancelledRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| UnreachableAdviceRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| CallingRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| OrganizationName | varchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| RegionName | varchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| FirstAdviceDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LastAdviceDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| BrandEnvoyDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TotalProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TotalServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ServiceRateAverage | decimal(18,2) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PortfolioOwnerName | varchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| SendUsedPointNotification | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TaxNo | varchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| TaxOffice | varchar(100) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| SmsPassword | varchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| PasswordOld | varchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LastPasswordChangeDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| Salt | varchar(50) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| MeskenCustomerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| LastMoveMesken | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| DeviceId | varchar(200) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| IsRepInfoConfirm | bit | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| RepInfoConfirmDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| SmsSendDate | datetime2(7) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |
| ActivationToken | varchar(400) | Evet |  | Hayir |  | Crm.Areas; Crm.NotificationGroupSubscriber; Crm.Organizations; Crm.Portfolios; Crm.RepCampaigns; Crm.RepContracts; Crm.RepIbans; Crm.RepPayments; Crm.Reps; Crm.Users |  |

## Crm.RestDays

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Users |  |
| Date | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.RiskTrackingCosts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| CostName | nvarchar(50) | Hayir |  | Hayir |  | Crm.Users |  |
| CostPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |

## Crm.RiskTrackingLawyers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.RiskTrackings; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RiskTrackings; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.RiskTrackings; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.RiskTrackings; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RiskTrackings; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RiskTrackings; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.RiskTrackings; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.RiskTrackings; Crm.Users |  |
| Name | nvarchar(400) | Hayir |  | Hayir |  | Crm.RiskTrackings; Crm.Users |  |

## Crm.RiskTrackings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| OrganizationName | nvarchar(50) | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| RegionUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| RegionName | nvarchar(50) | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| RiskTrackingLawyerUid | uniqueidentifier | Evet |  | Hayir | Crm.RiskTrackingLawyers.Uid | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| Status | smallint | Hayir | ((0)) | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SubStatus | smallint | Hayir | ((0)) | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| Year | smallint | Hayir |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| TotalReceivableAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| NotificationStatus | smallint | Hayir | ((0)) | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| FirstPostDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| FirstNotificationDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| FirstNoticeWageNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| FirstNoticeWageBarcodeNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| FirstPriceOfNotice | decimal(18,2) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SecondPostDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SecondNotificationDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SecondPetitionWageNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SecondPetitionWageBarcodeNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SecondPriceOfNotice | decimal(18,2) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| ExecutionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| PaymentStatus | bit | Hayir | ((0)) | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| ContractNo | nvarchar(50) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| ManagerApproveLimit | decimal(18,2) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| DelayStartInstallmentNumber | int | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| DelayEndInstallmentNumber | int | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| SynthTrackingAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| EnforcementProceedingAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| ClosedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| PaymentPromiseDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |
| IsSynth | bit | Evet | ((1)) | Hayir |  | Crm.Organizations; Crm.RiskTrackingLawyers; Crm.Users |  |

## Crm.Roles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| Key | nvarchar(50) | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| IsBranch | bit | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| Description | nvarchar(100) | Evet |  | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| HiddenReport | bit | Hayir | ((0)) | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |
| IsResponsibleBranch | bit | Hayir | ((0)) | Hayir |  | Crm.Authorities; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.RoleTargets; Crm.UserHistories; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.Users |  |

## Crm.RoleTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.Roles; Crm.Users |  |
| ReferanceTarget | int | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| AppointmentTarget | int | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| ContractTarget | int | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| Month | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| Year | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxReferanceScore | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxAppointmentScore | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxContractScore | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxGiroScore | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxReferanceScorePlus | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxAppointmentScorePlus | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxContractScorePlus | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxGiroScorePlus | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| BranchCategoryUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| PerformanceTarget | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxPerformanceScore | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| MaxPerformanceScorePlus | int | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |

## Crm.ScoreCards

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| TotalScore | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| MarketingCount | int | Hayir |  | Hayir |  |  |  |
| ReferanceCount | int | Hayir |  | Hayir |  |  |  |
| ReferanceTarget | int | Hayir |  | Hayir |  |  |  |
| AppointmentCount | int | Hayir |  | Hayir |  |  |  |
| AppointmentTarget | int | Hayir |  | Hayir |  |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |  |
| ContractTarget | int | Hayir |  | Hayir |  |  |  |
| ContractPrice | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| CancellationAmount | decimal(18,2) | Hayir |  | Hayir |  |  |  |
| CancellationCount | int | Evet |  | Hayir |  |  |  |
| CancellationRate | decimal(18,2) | Evet |  | Hayir |  |  |  |
| SeveranceAmount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| SeveranceCount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| SeveranceRate | decimal(18,2) | Evet |  | Hayir |  |  |  |
| ParticipationFeeAverage | decimal(18,2) | Evet |  | Hayir |  |  |  |
| CashSaleRate | decimal(18,2) | Evet |  | Hayir |  |  |  |
| CashSaleCount | int | Evet |  | Hayir |  |  |  |
| CashGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| InstallmentGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| SpreadGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| PiecesGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |  |
| CandidateCount | int | Evet |  | Hayir |  |  |  |
| HomeCandidateCount | int | Evet |  | Hayir |  |  |  |
| CarCandidateCount | int | Evet |  | Hayir |  |  |  |
| HomeCandidateRate | int | Evet |  | Hayir |  |  |  |
| FacebookCandidateCount | int | Evet |  | Hayir |  |  |  |
| InstagramCandidateCount | int | Evet |  | Hayir |  |  |  |
| GoogleCandidateCount | int | Evet |  | Hayir |  |  |  |
| OtherCandidateCount | int | Evet |  | Hayir |  |  |  |
| TabelaCount | int | Evet |  | Hayir |  |  |  |
| GoogleCandidateRate | int | Evet |  | Hayir |  |  |  |
| ExternalAppointmentCount | int | Evet |  | Hayir |  |  |  |
| Premium | decimal(18,2) | Evet |  | Hayir |  |  |  |
| PremiumMultiplier | decimal(18,2) | Evet |  | Hayir |  |  |  |
| TotalPremium | decimal(18,2) | Evet |  | Hayir |  |  |  |
| Month | int | Evet |  | Hayir |  |  |  |
| Year | int | Evet |  | Hayir |  |  |  |
| PerformancePoint | int | Evet |  | Hayir |  |  |  |
| PerformanceTarget | int | Evet |  | Hayir |  |  |  |
| ContractPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |  |
| ContractPriceUnPaid | decimal(18,2) | Evet |  | Hayir |  |  |  |
| MobileBrachCount | int | Evet |  | Hayir |  |  |  |

## Crm.ServiceConfigurationLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ServiceConfigurationUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Status | bit | Hayir |  | Hayir |  |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |  |

## Crm.ServiceConfigurations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Id | int | Hayir |  | Hayir |  | Crm.Users |  |
| Name | varchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Description | varchar(400) | Evet |  | Hayir |  | Crm.Users |  |
| Link | varchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Type | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| FrequencyType | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| Frequency | int | Hayir |  | Hayir |  | Crm.Users |  |
| StartDate | date | Hayir |  | Hayir |  | Crm.Users |  |
| EndDate | date | Hayir |  | Hayir |  | Crm.Users |  |
| WorkingStartDate | datetime | Evet |  | Hayir |  | Crm.Users |  |
| WorkingEndDate | datetime | Evet |  | Hayir |  | Crm.Users |  |
| Status | smallint | Evet |  | Hayir |  | Crm.Users |  |
| Parameters | varchar(400) | Evet |  | Hayir |  | Crm.Users |  |
| SpecialTimeType | smallint | Evet |  | Hayir |  | Crm.Users |  |
| SpecialStartDate | datetime | Evet |  | Hayir |  | Crm.Users |  |
| SpecialEndDate | datetime | Evet |  | Hayir |  | Crm.Users |  |
| SpecialTimeParameter | varchar(400) | Evet |  | Hayir |  | Crm.Users |  |
| Priority | int | Hayir |  | Hayir |  | Crm.Users |  |
| IsLogActive | bit | Hayir | ((0)) | Hayir |  | Crm.Users |  |
| ListItemCount | int | Hayir |  | Hayir |  | Crm.Users |  |

## Crm.ServiceLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| ServiceUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Result | nvarchar(max) | Evet |  | Hayir |  |  |  |

## Crm.ServiceOthers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |  |
| Period | int | Hayir |  | Hayir |  |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| Link | nvarchar(200) | Evet |  | Hayir |  |  |  |
| Body | nvarchar(200) | Evet |  | Hayir |  |  |  |
| Priority | int | Evet |  | Hayir |  |  |  |
| Status | smallint | Evet |  | Hayir |  |  |  |
| ProcessingStartDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| ProcessingEndDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| ServiceId | smallint | Evet |  | Hayir |  |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| StartHour | time(7) | Evet |  | Hayir |  |  |  |
| EndHour | time(7) | Evet |  | Hayir |  |  |  |

## Crm.ServiceRateRanges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Products; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid | Crm.Products; Crm.Users |  |
| StartMonth | int | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| EndMonth | int | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceRateForCEO | decimal(18,2) | Hayir |  | Hayir |  | Crm.Products; Crm.Users |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet |  | Hayir |  | Crm.Products; Crm.Users |  |

## Crm.Services

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  | Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Users |  |
| Period | int | Hayir |  | Hayir |  | Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| Link | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Body | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Priority | int | Evet |  | Hayir |  | Crm.Users |  |
| Status | smallint | Evet |  | Hayir |  | Crm.Users |  |
| ProcessingStartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| ProcessingEndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| ServiceId | smallint | Evet |  | Hayir |  | Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| StartHour | time(7) | Evet |  | Hayir |  | Crm.Users |  |
| EndHour | time(7) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.SetOffLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PetitionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| TransactionDate | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.Users |  |
| OldContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewProductUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldContractCreatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractCreatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldIsDraw | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewIsDraw | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldServiceType | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewServiceType | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewProductPrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewServicePrice | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Status | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| SubStatus | nvarchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Description | nvarchar(500) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Year | int | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| Month | int | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| ProductPriceDifference | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| ServicePriceDifference | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractStatus | nvarchar(3) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldContractTotalPaid | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| BidApprovalRole | varchar(5) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldContractServiceRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractServiceRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldContractSalesPerson | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractSalesPerson | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| PostVirmanQueueUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| OldContractSalesOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |
| NewContractSalesOrganizationUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Users |  |

## Crm.SetOffProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| SetOffLogUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| Department | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |  |
| SetOffProcessType | smallint | Hayir |  | Hayir |  |  |  |

## Crm.Simulations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| InstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| CachePrice | decimal(18,2) | Hayir |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |
| SimulationUid | uniqueidentifier | Evet |  | Hayir | Crm.Simulations.Uid | Crm.Customers; Crm.Simulations; Crm.Users |  |
| IsMesken | bit | Evet |  | Hayir |  | Crm.Customers; Crm.Simulations; Crm.Users |  |

## Crm.SmsGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| SmsTemplateUid | uniqueidentifier | Evet |  | Hayir | Crm.SmsTemplates.Uid | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| SearchQuery | nvarchar(100) | Evet |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |
| IsCompleted | bit | Hayir |  | Hayir |  | Crm.SmsLogs; Crm.SmsTemplates; Crm.Users |  |

## Crm.SmsLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| SmsGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.SmsGroups.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| IsSent | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir | Crm.Opportunities.Uid | Crm.Contracts; Crm.Customers; Crm.Leads; Crm.Opportunities; Crm.SmsGroups; Crm.Users |  |

## Crm.SmsTemplates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.SmsGroups; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsGroups; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsGroups; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SmsGroups; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Type | nvarchar(50) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Key | nvarchar(100) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| IsNotification | bit | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Title | nvarchar(100) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| Enabled | bit | Evet | ((0)) | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| IsSms | bit | Evet | ((0)) | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| TestPhoneNumber | nvarchar(10) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |
| PhoneJSonList | nvarchar(500) | Evet |  | Hayir |  | Crm.SmsGroups; Crm.Users |  |

## Crm.SmsVerificationCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Leads; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Leads; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Leads; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Leads; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Leads; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Leads; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid | Crm.Leads; Crm.Users |  |
| VerificationCode | nvarchar(50) | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| Type | smallint | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| MobilePhone | nvarchar(50) | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| ExpirationDateTime | datetime | Hayir |  | Hayir |  | Crm.Leads; Crm.Users |  |
| IsUsed | bit | Hayir | ((0)) | Hayir |  | Crm.Leads; Crm.Users |  |

## Crm.SustainabilityFeatureValues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.SustainabilityReports; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SustainabilityReports; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SustainabilityReports; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.SustainabilityReports; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| FeatureType | smallint | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| Key | nvarchar(50) | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| Name | nvarchar(100) | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |
| Order | int | Hayir |  | Hayir |  | Crm.SustainabilityReports; Crm.Users |  |

## Crm.SustainabilityReports

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir | Crm.Mortgages.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| MortgagePledgeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgagePledges.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| FeatureType | smallint | Hayir |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| FeatureValueUid | uniqueidentifier | Evet |  | Hayir | Crm.SustainabilityFeatureValues.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |
| VehicleRegistrationType | smallint | Evet |  | Hayir |  | Crm.Contracts; Crm.MortgagePledges; Crm.MortgageTypes; Crm.Mortgages; Crm.SustainabilityFeatureValues; Crm.Users |  |

## Crm.TakbisCity

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |  |

## Crm.TakbisHomeTown

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Status | nvarchar(250) | Evet |  | Hayir |  |  |  |
| Type | nvarchar(250) | Evet |  | Hayir |  |  |  |
| TownId | int | Evet |  | Hayir |  |  |  |
| IsActive | bit | Evet |  | Hayir |  |  |  |

## Crm.TakbisInsuranceCompanies

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |  |
| Name | nvarchar(250) | Evet |  | Hayir |  |  |  |

## Crm.TakbisTown

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |  |
| CityId | int | Evet |  | Hayir |  |  |  |

## Crm.TicketHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Tickets; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Tickets; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Tickets; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Tickets; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| TicketUid | uniqueidentifier | Hayir |  | Hayir | Crm.Tickets.Uid | Crm.Tickets; Crm.Users |  |
| UpdatedName | nvarchar(200) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| FieldName | nvarchar(100) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| OldValue | nvarchar(50) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |
| NewValue | nvarchar(50) | Evet |  | Hayir |  | Crm.Tickets; Crm.Users |  |

## Crm.Tickets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Title | nvarchar(max) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Description | nvarchar(max) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| RequestingPersonUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Priority | nvarchar(max) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Type | nvarchar(max) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| Status | nvarchar(max) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| DeadLine | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |
| CompletedBy | uniqueidentifier | Evet |  | Hayir |  | Crm.Organizations; Crm.TicketHistories; Crm.Users |  |

## Crm.tmpAllGroupInfo

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| Name | nvarchar(20) | Hayir |  | Hayir |  |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |  |
| GroupDate | datetime | Hayir |  | Hayir |  |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |  |
| Type | nvarchar(3) | Evet |  | Hayir |  |  |  |
| JokerCount | int | Hayir |  | Hayir |  |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |  |
| TotalSelectCount | int | Hayir |  | Hayir |  |  |  |
| ContractSelectCount | int | Hayir |  | Hayir |  |  |  |
| JokerSelectCount | int | Hayir |  | Hayir |  |  |  |
| MaxDeliveryDate | datetime | Evet |  | Hayir |  |  |  |
| SelectCount | int | Hayir |  | Hayir |  |  |  |
| LastOrganizationDate | datetime | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime | Evet |  | Hayir |  |  |  |
| MaxDeliveryLastInstallment | int | Hayir |  | Hayir |  |  |  |
| CreatedBy | nvarchar(100) | Evet |  | Hayir |  |  |  |
| ClosedBy | nvarchar(100) | Evet |  | Hayir |  |  |  |
| StartDate | datetime | Evet |  | Hayir |  |  |  |
| EndDate | datetime | Evet |  | Hayir |  |  |  |
| Status | nvarchar(3) | Evet |  | Hayir |  |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |  |
| NextDraw | nvarchar(4) | Evet |  | Hayir |  |  |  |
| MaxDeliveryMonth | int | Hayir |  | Hayir |  |  |  |
| FirstOrganizationDate | datetime | Evet |  | Hayir |  |  |  |
| LastDrawDate | datetime | Evet |  | Hayir |  |  |  |
| NextDrawDate | datetime | Evet |  | Hayir |  |  |  |
| NextDrawPeriod | nvarchar(4) | Evet |  | Hayir |  |  |  |
| BallCount | int | Hayir |  | Hayir |  |  |  |
| TotalDrawBall | int | Hayir |  | Hayir |  |  |  |

## Crm.UnauthorizedProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Users |  |
| ModuleKey | nvarchar(400) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |
| Key | nvarchar(400) | Evet |  | Hayir |  | Crm.Organizations; Crm.Users |  |

## Crm.UserHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir | Crm.Portfolios.Uid | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Organizations; Crm.Portfolios; Crm.Roles; Crm.Users |  |

## Crm.UserLeaveDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Evet | ((0)) | Hayir |  |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| StartHour | datetime2(7) | Evet |  | Hayir |  |  |  |
| EndHour | datetime2(7) | Evet |  | Hayir |  |  |  |
| AnnualLeaveModel | bit | Evet |  | Hayir |  |  |  |
| AnnualLeaveType | int | Evet |  | Hayir |  |  |  |
| Description | varchar(300) | Evet |  | Hayir |  |  |  |
| CancelDescription | varchar(300) | Evet |  | Hayir |  |  |  |
| Status | smallint | Evet |  | Hayir |  |  |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| CancelBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| ApprovalBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| ProxyUserUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| InternalFileUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| IsUser | bit | Evet |  | Hayir |  |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| SubStatus | smallint | Evet |  | Hayir |  |  |  |

## Crm.UserLeavePermission

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| AnnualLeaveModel | int | Evet |  | Hayir |  |  |  |
| AnnualLeaveType | int | Evet |  | Hayir |  |  |  |
| PermissionName | varchar(max) | Evet |  | Hayir |  |  |  |
| ProgressDay | int | Evet |  | Hayir |  |  |  |

## Crm.UserLeaves

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Evet | ((0)) | Hayir |  |  |  |
| Seniority | int | Evet |  | Hayir |  |  |  |
| DeservedLeave | int | Evet |  | Hayir |  |  |  |
| TotalDeservedLeave | int | Evet |  | Hayir |  |  |  |
| DelegatedPermission | decimal(18,2) | Evet |  | Hayir |  |  |  |
| PermissionUsed | decimal(18,2) | Evet |  | Hayir |  |  |  |
| RemainingLeave | decimal(18,2) | Evet |  | Hayir |  |  |  |
| IsUser | bit | Evet |  | Hayir |  |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |  |

## Crm.UserLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  |  |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  |  |  |
| IsCrm | bit | Evet |  | Hayir |  |  |  |
| IsLdap | bit | Evet |  | Hayir |  |  |  |

## Crm.UserPasswordHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |  |
| Salt | varchar(100) | Evet |  | Hayir |  |  |  |
| ExpireDate | datetime2(7) | Evet |  | Hayir |  |  |  |
| HashType | smallint | Evet |  | Hayir |  |  |  |
| Platform | smallint | Evet |  | Hayir |  |  |  |

## Crm.UserPortfolios

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Portfolios; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Portfolios; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Portfolios; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Portfolios; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Portfolios; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Portfolios; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Portfolios; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Portfolios; Crm.Users |  |
| UserUid1 | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Portfolios; Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  | Crm.Portfolios; Crm.Users |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid | Crm.Portfolios; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Portfolios; Crm.Users |  |

## Crm.UserResponsibleBranches

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Organizations; Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Organizations; Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Organizations; Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir | ((0)) | Hayir |  | Crm.Organizations; Crm.Roles; Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| BranchUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Organizations; Crm.Roles; Crm.Users |  |

## Crm.UserRoles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Roles; Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Roles; Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Roles; Crm.Users |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid | Crm.Roles; Crm.Users |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Roles; Crm.Users |  |

## Crm.Users

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| EMail | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| HomePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Gender | nvarchar(10) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| UserName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Password | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| NewPassword | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IsUser | bit | Hayir |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LastCustomerAssignDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LastBranchCustomerAssignDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IsBusy | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| EMail2 | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Code | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IsManager | bit | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LastAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| InternalPhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Image | nvarchar(200) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Tckno | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IBAN | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| CostCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| CurrentCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| DateOfBirth | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LastDeskAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| RepCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| PartnerName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| PartnerTc | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| PartnerPhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| SamAccountName | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| ResetLdapPassword | bit | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| ResetPassword | bit | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| FirstName | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| Surname | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LoginFailedCount | smallint | Hayir | ((0)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| SecondCurrentCode | nvarchar(100) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| UType | int | Hayir | ((1)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IsVisibleMobilePhone | bit | Hayir | ((1)) | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| PrivatePhone | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LeaveType | smallint | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| LeaveSubType | int | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| IsNewHash | bit | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |
| OutSourceEmail | nvarchar(50) | Evet |  | Hayir |  | Crm.Activities; Crm.ActivityRecords; Crm.ActivityTypes; Crm.AdForms; Crm.Advices; Crm.Announcement; Crm.AppointmentAssignments; Crm.Areas; Crm.AssignedBidApprovers; Crm.Authorities; Crm.BankDetails; Crm.BankLogs; Crm.Banks; Crm.BidInstallments; Crm.BranchCategories; Crm.CampaignBranches; Crm.CampaignItems; Crm.CampaignSources; Crm.Campaigns; Crm.CashPriceIntervalRates; Crm.ComplaintNotes; Crm.Complaints; Crm.ContractLeavingLogs; Crm.ContractLeavings; Crm.ContractProductDeliveryRange; Crm.ContractProducts; Crm.ContractRevisions; Crm.ContractTemplate; Crm.ContractTemplateVariables; Crm.CostForms; Crm.CostItems; Crm.CostTypes; Crm.Costs; Crm.CustomerLoginFaileds; Crm.CustomerLoginSmsFaileds; Crm.CustomerLogins; Crm.CustomerSources; Crm.Customers; Crm.DailyServicePricePaidLogs; Crm.DataAnalysisLogs; Crm.Debits; Crm.Deliveries; Crm.DeliveryCallHistories; Crm.DeliveryCallNotes; Crm.DeliveryCalls; Crm.DeliveryEmployees; Crm.DeliveryFiles; Crm.DeliveryPayments; Crm.DeliveryRanges; Crm.DeliveryWorkAdvances; Crm.Distraints; Crm.Documents; Crm.DrawCodes; Crm.Draws; Crm.ETesisTerkinContractIbans; Crm.ETesisTerkinIntegrations; Crm.FileTypeCategories; Crm.FileTypes; Crm.Files; Crm.Firms; Crm.GroupProducts; Crm.Groups; Crm.Guarantors; Crm.IntegrationApiLogs; Crm.IntegrationApiLogs250919; Crm.InternetSubeLogs; Crm.Inventories; Crm.InventoryDebits; Crm.InventoryTypes; Crm.InvoiceLogoLogs; Crm.IssueHistories; Crm.Issues; Crm.LeadForms; Crm.LoginFaileds; Crm.Logins; Crm.LogoLogs; Crm.LogoPayments; Crm.LogoServiceLogs; Crm.ManuelLeadForCallCenterQueues; Crm.MobileApplicationConfigurations; Crm.MobileConfigurationSettings; Crm.MobilePhoneNumbers; Crm.ModuleAuths; Crm.Modules; Crm.MortgageCosts; Crm.MortgageInsurances; Crm.MortgageLogs; Crm.MortgagePledgeVehicleBrandModels; Crm.MortgageTypes; Crm.Mortgages; Crm.Nationalities; Crm.NotaryLists; Crm.NotaryResults; Crm.NotificationGroupSubscriber; Crm.NotificationGroups; Crm.NotificationLogs; Crm.NotificationVariables; Crm.Occupations; Crm.OffsetLogs; Crm.OnlineUsers; Crm.Opportunities; Crm.OrganizationAreas; Crm.OrganizationHistories; Crm.OrganizationMonthlyTargets; Crm.Organizations; Crm.Performances; Crm.PlannedPeriodicDeliveryAmounts; Crm.Portfolios; Crm.PosPayments; Crm.PostVirmanQueues; Crm.PremiumBranchRates; Crm.PremiumContracts; Crm.PremiumItems; Crm.PremiumTimingGroups; Crm.PremiumTimings; Crm.PremiumUserTypeRates; Crm.Premiums; Crm.Products; Crm.QualityAnswers; Crm.QualityForms; Crm.QualityNotes; Crm.QualityQuestions; Crm.RepContracts; Crm.RepGifts; Crm.RepIbans; Crm.RepPaymentDetails; Crm.RepPaymentGroups; Crm.RepPayments; Crm.RepPointLogs; Crm.RepPoints; Crm.Reps; Crm.RestDays; Crm.RiskTrackingCosts; Crm.RiskTrackingLawyers; Crm.RiskTrackings; Crm.RoleTargets; Crm.Roles; Crm.ServiceConfigurations; Crm.ServiceRateRanges; Crm.Services; Crm.SetOffLogs; Crm.Simulations; Crm.SmsGroups; Crm.SmsLogs; Crm.SmsTemplates; Crm.SmsVerificationCodes; Crm.SustainabilityFeatureValues; Crm.SustainabilityReports; Crm.TicketHistories; Crm.Tickets; Crm.UnauthorizedProcessLogs; Crm.UserHistories; Crm.UserPortfolios; Crm.UserResponsibleBranches; Crm.UserRoles; Crm.UserTargets; Crm.Users; Crm.VariableIndexGroups; Crm.VariableIndexs; Crm.VirtualPosCommisions; Crm.VirtualPosLogs |  |

## Crm.UserTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| ReferanceTarget | int | Hayir |  | Hayir |  | Crm.Users |  |
| AppointmentTarget | int | Hayir |  | Hayir |  | Crm.Users |  |
| ContractTarget | int | Hayir |  | Hayir |  | Crm.Users |  |
| Month | int | Hayir |  | Hayir |  | Crm.Users |  |
| Year | int | Hayir |  | Hayir |  | Crm.Users |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| MaxReferanceScore | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxAppointmentScore | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxContractScore | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxGiroScore | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxReferanceScorePlus | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxAppointmentScorePlus | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxContractScorePlus | int | Hayir |  | Hayir |  | Crm.Users |  |
| MaxGiroScorePlus | int | Hayir |  | Hayir |  | Crm.Users |  |
| PerformanceTarget | int | Evet |  | Hayir |  | Crm.Users |  |
| MaxPerformanceScore | int | Evet |  | Hayir |  | Crm.Users |  |
| MaxPerformanceScorePlus | int | Evet |  | Hayir |  | Crm.Users |  |

## Crm.VariableIndexGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| Name | nvarchar(100) | Evet |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| ShortName | nvarchar(100) | Evet |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |
| IsRate | bit | Hayir |  | Hayir |  | Crm.Products; Crm.Users; Crm.VariableIndexs |  |

## Crm.VariableIndexs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users; Crm.VariableIndexGroups |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users; Crm.VariableIndexGroups |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users; Crm.VariableIndexGroups |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users; Crm.VariableIndexGroups |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| Value | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| Date | datetime2(7) | Hayir |  | Hayir |  | Crm.Users; Crm.VariableIndexGroups |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.VariableIndexGroups.Uid | Crm.Users; Crm.VariableIndexGroups |  |

## Crm.VirtualPosCommisions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| BanklogUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| TotalAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| CommisionAmount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| CommisionRate | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| CashCommisionRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |
| CashCommisionAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |

## Crm.VirtualPosLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Iliskili Tablolar | Not |
|---|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  | Crm.Users |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  | Crm.Users |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid | Crm.Users |  |
| Deleted | bit | Hayir |  | Hayir |  | Crm.Users |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| MerchantID | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  | Crm.Users |  |
| MD | nvarchar(500) | Evet |  | Hayir |  | Crm.Users |  |
| HashData | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Response | nvarchar(100) | Evet |  | Hayir |  | Crm.Users |  |
| ProvisionNumber | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| RRN | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Stan | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| ResponseMessage | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| ResponseCode | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| MerchantOrderId | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| BankCode | nvarchar(200) | Evet |  | Hayir |  | Crm.Users |  |
| Status | smallint | Hayir |  | Hayir |  | Crm.Users |  |
| Message | nvarchar(max) | Evet |  | Hayir |  | Crm.Users |  |
| BankLogUid | uniqueidentifier | Evet |  | Hayir |  | Crm.Users |  |
| InQueue | bit | Hayir | ((0)) | Hayir |  | Crm.Users |  |
| CommisionAmount | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Users |  |
| CommisionRate | decimal(18,2) | Hayir | ((0)) | Hayir |  | Crm.Users |  |
| InstallmentCount | int | Evet | ((1)) | Hayir |  | Crm.Users |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  | Crm.Users |  |
| CashCommisionRate | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |
| CashCommisionAmount | decimal(18,2) | Evet |  | Hayir |  | Crm.Users |  |
| CanPayServicePriceInstbyVP | bit | Evet |  | Hayir |  | Crm.Users |  |
| LogoStatus | smallint | Evet |  | Hayir |  | Crm.Users |  |
| PosId | int | Evet |  | Hayir |  | Crm.Users |  |

