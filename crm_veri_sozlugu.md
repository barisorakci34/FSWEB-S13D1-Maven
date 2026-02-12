# CRM Veri Sozlugu

- Uretim tarihi: 2026-02-12 08:41:05
- Kaynak dosya: `/home/ubuntu/.cursor/projects/workspace/uploads/script.txt`
- Veritabani: `katilim.crm`
- Kapsam: `Crm` semasindaki tablolar
- Toplam tablo: **213**
- Toplam kolon: **4516**
- Toplam PK kolonu: **203**
- Toplam FK baglantisi: **719**

> Not: Bu sozluk, SQL DDL scriptinden otomatik uretilmistir.

## Crm.AccountingCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Period | nvarchar(9) | Hayir |  | Hayir |  |  |
| Type | nvarchar(9) | Hayir |  | Hayir |  |  |
| Model | nvarchar(9) | Hayir |  | Hayir |  |  |
| DueType | nvarchar(9) | Hayir |  | Hayir |  |  |
| Key | nvarchar(20) | Hayir |  | Hayir |  |  |
| Code | nvarchar(20) | Hayir |  | Hayir |  |  |
| Description | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.Activities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ActivityTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid |  |
| ActivitySubTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid |  |
| Status | nvarchar(1) | Evet |  | Hayir |  |  |
| ResultType | nvarchar(2) | Evet |  | Hayir |  |  |
| SuccessBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CanceledBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| IsImportant | bit | Hayir |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DescriptionDone | nvarchar(4000) | Evet |  | Hayir |  |  |
| IsAppointmentCall | bit | Hayir | ((0)) | Hayir |  |  |
| IsAttendedTheMeeting | bit | Hayir | ((0)) | Hayir |  |  |
| IsSequent | bit | Hayir | ((0)) | Hayir |  |  |
| ReasonDescription | nvarchar(4000) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir | Crm.Opportunities.Uid |  |
| OldCustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsSMS | bit | Hayir | ((0)) | Hayir |  |  |
| IsSoundRecord | bit | Hayir | ((0)) | Hayir |  |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FirstAppointment | bit | Evet |  | Hayir |  |  |
| AppointmentAssignmentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| WillAttend | bit | Evet |  | Hayir |  |  |
| ComplaintUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| LastMoveMesken | bit | Evet |  | Hayir |  |  |
| CounterEndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.ActivityRecords

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| FileName | nvarchar(500) | Evet |  | Hayir |  |  |
| FileSize | decimal(18,2) | Hayir |  | Hayir |  |  |
| ActivityUid | uniqueidentifier | Hayir |  | Hayir | Crm.Activities.Uid |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| Duration | int | Evet |  | Hayir |  |  |
| NewFileName | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.ActivityTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| isSystem | bit | Hayir |  | Hayir |  |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.ActivityTypes.Uid |  |

## Crm.AdForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| LastUpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| LastUpdateCount | int | Hayir | ((0)) | Hayir |  |  |
| BlockDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.Advices

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| IsDetailShared | bit | Evet |  | Hayir |  |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  |  |
| IsBulkInvitation | bit | Evet |  | Hayir |  |  |
| IsProductDetail | bit | Evet |  | Hayir |  |  |
| ProductType | varchar(1) | Evet |  | Hayir |  |  |
| ProductPrice | varchar(10) | Evet |  | Hayir |  |  |
| InstallmentPrice | varchar(10) | Evet |  | Hayir |  |  |
| AdvancePayment | varchar(10) | Evet |  | Hayir |  |  |
| CancelledLink | bit | Evet |  | Hayir |  |  |
| CancelledLinkDate | datetime | Evet |  | Hayir |  |  |
| ProcessDate | datetime | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.AllGroupInfo

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Name | nvarchar(20) | Hayir |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| GroupDate | varchar(10) | Evet |  | Hayir |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(3) | Evet |  | Hayir |  |  |
| JokerCount | int | Hayir |  | Hayir |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |
| TotalSelectCount | int | Hayir |  | Hayir |  |  |
| ContractSelectCount | int | Hayir |  | Hayir |  |  |
| JokerSelectCount | int | Hayir |  | Hayir |  |  |
| MaxDeliveryDate | varchar(10) | Evet |  | Hayir |  |  |
| SelectCount | int | Hayir |  | Hayir |  |  |
| LastOrganizationDate | varchar(10) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| MaxDeliveryLastInstallment | int | Hayir |  | Hayir |  |  |
| CreatedBy | nvarchar(100) | Evet |  | Hayir |  |  |
| ClosedBy | nvarchar(100) | Evet |  | Hayir |  |  |
| StartDate | varchar(10) | Evet |  | Hayir |  |  |
| EndDate | varchar(10) | Evet |  | Hayir |  |  |
| Status | nvarchar(3) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| NextDraw | nvarchar(4) | Evet |  | Hayir |  |  |
| MaxDeliveryMonth | int | Hayir |  | Hayir |  |  |
| FirstOrganizationDate | varchar(10) | Evet |  | Hayir |  |  |
| LastDrawDate | varchar(10) | Evet |  | Hayir |  |  |
| NextDrawDate | varchar(10) | Evet |  | Hayir |  |  |
| NextDrawPeriod | nvarchar(4) | Evet |  | Hayir |  |  |
| BallCount | int | Hayir |  | Hayir |  |  |
| TotalDrawBall | int | Hayir |  | Hayir |  |  |

## Crm.Announcement

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Title | nvarchar(4000) | Evet |  | Hayir |  |  |
| Image | nvarchar(500) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| ShortDescription | nvarchar(4000) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Channel | int | Evet |  | Hayir |  |  |
| IsPopup | bit | Evet |  | Hayir |  |  |
| AnnouncementType | int | Evet |  | Hayir |  |  |
| AnnouncementStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| AnnouncementEndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.ApplicationConfiguration

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Key | nvarchar(400) | Evet |  | Hayir |  |  |
| Value | nvarchar(max) | Evet |  | Hayir |  |  |
| Platform | smallint | Hayir |  | Hayir |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.ApplicationLoginLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| AppId | smallint | Evet |  | Hayir |  |  |
| PlatformId | smallint | Evet |  | Hayir |  |  |
| AppVersion | nvarchar(10) | Evet |  | Hayir |  |  |
| IsFailed | bit | Hayir |  | Hayir |  |  |
| Message | nvarchar(400) | Evet |  | Hayir |  |  |

## Crm.AppointmentAssignments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AssignDate | datetime2(7) | Hayir |  | Hayir |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |
| CustomerTypeId | int | Hayir |  | Hayir |  |  |

## Crm.Areas

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| NameEn | nvarchar(100) | Evet |  | Hayir |  |  |
| Code | nvarchar(20) | Evet |  | Hayir |  |  |
| Type | nvarchar(10) | Evet |  | Hayir |  |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| Point | int | Hayir | ((0)) | Hayir |  |  |

## Crm.AssignedBidApprovers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BidUid | uniqueidentifier | Evet |  | Hayir | Crm.Bids.Uid |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  |  |
| ProductInstallmentCount | int | Hayir |  | Hayir |  |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  |  |
| BidCreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.Authorities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| RoleUid | uniqueidentifier | Evet |  | Hayir | Crm.Roles.Uid |  |
| ModuleAuthUid | uniqueidentifier | Hayir |  | Hayir | Crm.ModuleAuths.Uid |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.BankDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| BankUid | uniqueidentifier | Evet |  | Hayir | Crm.Banks.Uid |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.BankLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| MdStatus | int | Hayir |  | Hayir |  |  |
| TRANID | nvarchar(100) | Evet |  | Hayir |  |  |
| PAResSyntaxOK | bit | Evet |  | Hayir |  |  |
| MerchantID | nvarchar(100) | Evet |  | Hayir |  |  |
| MaskedCreditCard | nvarchar(100) | Evet |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| sID | int | Evet |  | Hayir |  |  |
| ACQBIN | nvarchar(100) | Evet |  | Hayir |  |  |
| Ecom_Payment_Card_ExpDate_Year | int | Evet |  | Hayir |  |  |
| Ecom_Payment_Card_ExpDate_Month | int | Evet |  | Hayir |  |  |
| MaskedPan | nvarchar(100) | Evet |  | Hayir |  |  |
| ClientIp | nvarchar(100) | Evet |  | Hayir |  |  |
| iReqDetail | nvarchar(100) | Evet |  | Hayir |  |  |
| Md | nvarchar(500) | Evet |  | Hayir |  |  |
| VendorCode | nvarchar(100) | Evet |  | Hayir |  |  |
| Storetype | nvarchar(100) | Evet |  | Hayir |  |  |
| IReqCode | nvarchar(100) | Evet |  | Hayir |  |  |
| MdErrorMsg | nvarchar(500) | Evet |  | Hayir |  |  |
| PAResVerified | bit | Evet |  | Hayir |  |  |
| Cavv | nvarchar(100) | Evet |  | Hayir |  |  |
| Digest | nvarchar(100) | Evet |  | Hayir |  |  |
| CallbackCall | bit | Evet |  | Hayir |  |  |
| CavvAlgorithm | nvarchar(100) | Evet |  | Hayir |  |  |
| Cid | nvarchar(max) | Evet |  | Hayir |  |  |
| Encoding | nvarchar(100) | Evet |  | Hayir |  |  |
| Currency | nvarchar(100) | Evet |  | Hayir |  |  |
| DsId | nvarchar(100) | Evet |  | Hayir |  |  |
| Eci | nvarchar(100) | Evet |  | Hayir |  |  |
| Version | nvarchar(100) | Evet |  | Hayir |  |  |
| Clientid | nvarchar(100) | Evet |  | Hayir |  |  |
| Txstatus | nvarchar(100) | Evet |  | Hayir |  |  |
| Charset | nvarchar(100) | Evet |  | Hayir |  |  |
| Hash | nvarchar(100) | Evet |  | Hayir |  |  |
| Rnd | nvarchar(100) | Evet |  | Hayir |  |  |
| HASHPARAMS | nvarchar(500) | Evet |  | Hayir |  |  |
| HASHPARAMSVAL | nvarchar(500) | Evet |  | Hayir |  |  |
| ErrMsg | nvarchar(500) | Evet |  | Hayir |  |  |
| Response | nvarchar(100) | Evet |  | Hayir |  |  |
| ProcReturnCode | int | Hayir |  | Hayir |  |  |
| ErrCode | nvarchar(100) | Evet |  | Hayir |  |  |
| FailUrl | nvarchar(100) | Evet |  | Hayir |  |  |
| OkUrl | nvarchar(100) | Evet |  | Hayir |  |  |
| Lang | nvarchar(100) | Evet |  | Hayir |  |  |
| Xid | nvarchar(100) | Evet |  | Hayir |  |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  |  |
| AuthCode | nvarchar(100) | Evet |  | Hayir |  |  |
| HostRefNum | nvarchar(100) | Evet |  | Hayir |  |  |
| TransId | nvarchar(100) | Evet |  | Hayir |  |  |
| HOSTMSG | nvarchar(100) | Evet |  | Hayir |  |  |
| ProvisionNumber | nvarchar(200) | Evet |  | Hayir |  |  |
| HashData | nvarchar(200) | Evet |  | Hayir |  |  |
| RRN | nvarchar(200) | Evet |  | Hayir |  |  |
| Stan | nvarchar(200) | Evet |  | Hayir |  |  |
| ResponseMessage | nvarchar(200) | Evet |  | Hayir |  |  |
| ResponseCode | nvarchar(200) | Evet |  | Hayir |  |  |
| MerchantOrderId | nvarchar(200) | Evet |  | Hayir |  |  |
| BankCode | nvarchar(200) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |

## Crm.Banks

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.BidInstallments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| BidUid | uniqueidentifier | Evet |  | Hayir | Crm.Bids.Uid |  |
| InstallmentNumber | int | Hayir |  | Hayir |  |  |
| Price | decimal(18,2) | Evet |  | Hayir |  |  |
| DueDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| IsLast | bit | Hayir |  | Hayir |  |  |
| RemainingAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| Editable | bit | Evet |  | Hayir |  |  |
| Sub_Type | nvarchar(10) | Evet |  | Hayir |  |  |
| Sub_InstallmentNumber | int | Evet |  | Hayir |  |  |

## Crm.Bids

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| SimulationUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| InstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CachePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  |  |
| ServiceRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForBranchLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForRegionLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateNotCampaign | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateNotCampaignLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServicePriceNotCampaign | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServicePriceNotCampaignLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServicePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServicePriceLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateLast | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  |  |
| ServiceNewRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceNewPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceNewInstallmentCount | int | Hayir |  | Hayir |  |  |
| ServiceMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ServiceLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ServiceError | bit | Hayir |  | Hayir |  |  |
| ServiceMessage | nvarchar(500) | Evet |  | Hayir |  |  |
| ReelProductInstallmentCount | int | Hayir |  | Hayir |  |  |
| CashRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  |  |
| CashNewRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashNewPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashNewInstallmentCount | int | Hayir |  | Hayir |  |  |
| CashMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| CashLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| CashError | bit | Hayir |  | Hayir |  |  |
| CashMessage | nvarchar(500) | Evet |  | Hayir |  |  |
| Endeks | decimal(18,2) | Hayir |  | Hayir |  |  |
| Total | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductInstallmentCount | int | Hayir |  | Hayir |  |  |
| ProductInstallmentPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ProductNewRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductNewPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductNewInstallmentCount | int | Hayir |  | Hayir |  |  |
| ProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| FirstInstallmentRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ProductLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ProductError | bit | Hayir |  | Hayir |  |  |
| ProductMessage | nvarchar(4000) | Evet |  | Hayir |  |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| DeliveryLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| DeliveryFirstInstallmentNotCampaign | int | Hayir |  | Hayir |  |  |
| DeliveryLastInstallmentNotCampaign | int | Hayir |  | Hayir |  |  |
| DeliveryFirstInstallmentDateNotCampaign | datetime2(7) | Hayir |  | Hayir |  |  |
| DeliveryLastInstallmentDateNotCampaign | datetime2(7) | Hayir |  | Hayir |  |  |
| ServiceFirstInstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| DelayingDeliveryMonth | int | Hayir |  | Hayir |  |  |
| ProductLog | nvarchar(500) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| IsSMS | bit | Hayir |  | Hayir |  |  |
| IsContract | bit | Hayir |  | Hayir |  |  |
| IsActive | bit | Evet |  | Hayir |  |  |
| ApprovalRole | varchar(2) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ServiceRateForCEO | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsDistance | bit | Evet |  | Hayir |  |  |
| IsApproved | bit | Evet |  | Hayir |  |  |
| CustomerApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| ConvertToContractDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsCanBeEdited | bit | Evet | ((1)) | Hayir |  |  |
| ServiceRateWithOutCashPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MinServiceRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| MinServicePriceForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| IsFirstService | bit | Evet |  | Hayir |  |  |
| RejectReason | nvarchar(4000) | Evet |  | Hayir |  |  |
| FirstProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| InflationIncreaseCount | int | Evet |  | Hayir |  |  |
| PreliminaryInformationDate | datetime2(7) | Evet |  | Hayir |  |  |
| PreInfoIsApproved | bit | Evet |  | Hayir |  |  |
| OldProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ContractDurationMonth | smallint | Evet |  | Hayir |  |  |
| PaidInstallmentCount | smallint | Evet |  | Hayir |  |  |
| RemainingServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| RemainingServiceInstallmentCount | smallint | Evet |  | Hayir |  |  |
| NewContractStartDate | datetime | Evet |  | Hayir |  |  |
| PaidServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| CachePriceAddition | decimal(18,2) | Evet |  | Hayir |  |  |
| TmsfFirmId | smallint | Evet |  | Hayir |  |  |
| ServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |
| FirstServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |
| ServiceFirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  |  |
| FragmentationServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |

## Crm.BranchCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.CampaignBranches

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CampaignUid | uniqueidentifier | Hayir |  | Hayir | Crm.Campaigns.Uid |  |
| BranchUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |

## Crm.CampaignItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CampaignSourceUid | uniqueidentifier | Hayir |  | Hayir | Crm.CampaignSources.Uid |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Link | nvarchar(500) | Evet |  | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| Images | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.CampaignName

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| CampaignNameHome | nvarchar(50) | Evet |  | Hayir |  |  |
| CampaignNameCar | nvarchar(50) | Evet |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Evet |  | Hayir |  |  |
| Uid | uniqueidentifier | Evet |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.Campaigns

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| CountOfTargetedAppeal | int | Evet |  | Hayir |  |  |
| CountOfTargetedLead | int | Evet |  | Hayir |  |  |
| CountOfTargetedOpportunity | int | Evet |  | Hayir |  |  |
| TargetedPotential | decimal(18,2) | Evet |  | Hayir |  |  |
| TargetedGiro | decimal(18,2) | Evet |  | Hayir |  |  |
| Budget | decimal(18,2) | Evet |  | Hayir |  |  |
| Key | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.CampaignSources

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CampaignUid | uniqueidentifier | Hayir |  | Hayir | Crm.Campaigns.Uid |  |
| SourceUid | uniqueidentifier | Hayir |  | Hayir | Crm.CustomerSources.Uid |  |

## Crm.CashPriceIntervalRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ReelRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid |  |

## Crm.CodeExplanations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | int | Hayir |  | Evet |  | Identity |
| Description | varchar(100) | Evet |  | Hayir |  |  |
| Type | tinyint | Hayir |  | Hayir |  |  |
| No | tinyint | Hayir |  | Hayir |  |  |
| Code | varchar(20) | Hayir |  | Hayir |  |  |
| Name | varchar(100) | Hayir |  | Hayir |  |  |
| Explanation | varchar(100) | Evet |  | Hayir |  |  |

## Crm.ComplaintHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Subject | nvarchar(4000) | Evet |  | Hayir |  |  |
| Explanation | nvarchar(4000) | Evet |  | Hayir |  |  |
| IsAnswer | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Answer | nvarchar(4000) | Evet |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ComplaintUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| AssignedPersonUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |
| SubStatus | varchar(2) | Evet |  | Hayir |  |  |
| FieldNameText | nvarchar(100) | Evet |  | Hayir |  |  |
| OldValueText | nvarchar(100) | Evet |  | Hayir |  |  |
| NewValueText | nvarchar(100) | Evet |  | Hayir |  |  |
| TransactionName | nvarchar(100) | Evet |  | Hayir |  |  |
| OldValue | nvarchar(4000) | Evet |  | Hayir |  |  |
| NewValue | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.ComplaintNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| ComplaintUid | uniqueidentifier | Hayir |  | Hayir | Crm.Complaints.Uid |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir | ((0)) | Hayir |  |  |
| Name | nvarchar(1000) | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.Complaints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Subject | nvarchar(4000) | Evet |  | Hayir |  |  |
| Explanation | nvarchar(4000) | Evet |  | Hayir |  |  |
| IsAnswer | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Answer | nvarchar(4000) | Evet |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |
| AssignedPersonUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Source | nvarchar(50) | Evet |  | Hayir |  |  |
| Priority | nvarchar(50) | Evet |  | Hayir |  |  |
| CancellationReason | nvarchar(50) | Evet |  | Hayir |  |  |
| ComplaintNo | nvarchar(8) | Evet |  | Hayir |  |  |
| DirectCompleteDate | datetime2(7) | Evet |  | Hayir |  |  |
| SubStatus | nvarchar(2) | Evet |  | Hayir |  |  |
| Referrer | uniqueidentifier | Evet |  | Hayir |  |  |
| ReferrersDepartment | uniqueidentifier | Evet |  | Hayir |  |  |
| RelatedComplaints | uniqueidentifier | Evet |  | Hayir |  |  |
| SmsCount | int | Evet |  | Hayir |  |  |
| OutBandCallUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CallCount | int | Evet |  | Hayir |  |  |
| SubjectCategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SikayetvarNo | int | Evet |  | Hayir |  |  |
| SikayetvarName | nvarchar(255) | Evet |  | Hayir |  |  |

## Crm.ComplaintsSubjectCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Type | char(1) | Hayir |  | Hayir |  |  |
| SubjectCategoryName | nvarchar(250) | Hayir |  | Hayir |  |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |

## Crm.ContractDocumentIssues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Description | nvarchar(max) | Evet |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Status | int | Hayir |  | Hayir |  |  |

## Crm.ContractIBANs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| IBAN | nvarchar(150) | Evet |  | Hayir |  |  |
| BankName | nvarchar(150) | Evet |  | Hayir |  |  |
| Name | nvarchar(150) | Evet |  | Hayir |  |  |
| Surname | nvarchar(150) | Evet |  | Hayir |  |  |
| SellerIBAN | nvarchar(150) | Evet |  | Hayir |  |  |
| SellerBankName | nvarchar(250) | Evet |  | Hayir |  |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  |  |
| FatherName | nvarchar(100) | Evet |  | Hayir |  |  |
| Type | smallint | Hayir | ((1)) | Hayir |  |  |
| IsCompany | bit | Evet |  | Hayir |  |  |
| SalesPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| SellerTckno | nvarchar(11) | Evet |  | Hayir |  |  |
| SellerTaxNo | nvarchar(10) | Evet |  | Hayir |  |  |

## Crm.ContractLeavingLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractLeavingLogType | smallint | Evet |  | Hayir |  |  |
| Department | nvarchar(100) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.ContractLeavings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| BeforeReturnContractStatus | nvarchar(50) | Evet |  | Hayir |  |  |
| BeforeReturnGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ReturnStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| ReturnMoneyH | decimal(18,2) | Evet |  | Hayir |  |  |
| ReturnMoneyO | decimal(18,2) | Evet |  | Hayir |  |  |
| ReturnMoneyP | decimal(18,2) | Evet |  | Hayir |  |  |
| ReturnMoneyA | decimal(18,2) | Evet |  | Hayir |  |  |
| ReturnMoneyS | decimal(18,2) | Evet |  | Hayir |  |  |
| InternalAudit | smallint | Evet |  | Hayir |  |  |
| InternalAuditProcessDate | datetime2(7) | Evet |  | Hayir |  |  |
| InternalAuditProcessedBy | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.ContractProductDeliveryRange

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| StartMonth | int | Hayir |  | Hayir |  |  |
| EndMonth | int | Hayir |  | Hayir |  |  |
| StartMonthNotCampaign | int | Hayir |  | Hayir |  |  |
| EndMonthNotCampaign | int | Hayir |  | Hayir |  |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ContractProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.ContractProducts.Uid |  |

## Crm.ContractProducts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  |  |
| CashRateForBranch | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| ContractHtml | nvarchar(max) | Evet |  | Hayir |  |  |
| DeliveryMonth | int | Hayir |  | Hayir |  |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Model | nvarchar(50) | Evet |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| IncreaseRateAfterDelivery | decimal(18,2) | Hayir |  | Hayir |  |  |
| FixedIndex | decimal(18,2) | Evet |  | Hayir |  |  |
| VariableIndexGroup | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  |  |
| Status | nvarchar(max) | Evet |  | Hayir |  |  |
| ServiceRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| DistributedCashRate | int | Evet |  | Hayir |  |  |
| ServiceRateForBranchFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceDivided | bit | Evet |  | Hayir |  |  |
| ServiceRateForCEOFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceDividedUntilDelivery | bit | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| MinProductPriceForDeliveryDistributed | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceChargedBeforeDelivery | bit | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceDistributed | bit | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| MinProductPriceForDistributed | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| FlexibleDeliveryRate | decimal(18,2) | Evet |  | Hayir |  |  |
| IsActive | bit | Evet |  | Hayir |  |  |
| PremiumRate | decimal(18,2) | Evet |  | Hayir |  |  |
| IncreaseRateBeforeDelivery | decimal(18,2) | Evet |  | Hayir |  |  |
| IncreaseRateAfterDeliveryArray | nvarchar(max) | Evet |  | Hayir |  |  |
| MinProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MaxProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| GroupLimit | int | Evet |  | Hayir |  |  |
| DownPaymentUpperLimit | int | Evet |  | Hayir |  |  |
| ServicePriceLoweLimit | int | Evet |  | Hayir |  |  |
| Featured | bit | Evet |  | Hayir |  |  |
| PointServiceRateLimit | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.ContractRevisions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| Month | int | Hayir |  | Hayir |  |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProccesType | nvarchar(50) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid |  |
| ControllerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| ControllerDate | datetime2(7) | Evet |  | Hayir |  |  |
| ExtraServicePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ExtraCashPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ExtraProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| TotalExtraPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| NewDeliveryDateRange | nvarchar(200) | Evet |  | Hayir |  |  |
| NewDeliveryMonth | int | Evet |  | Hayir |  |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeliveryLastInstallmentDate | datetime2(7) | Evet |  | Hayir |  |  |
| ScheduledDeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| NewContractNo | nvarchar(20) | Evet |  | Hayir |  |  |
| OldContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| TransferedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| SnapshotContractPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| Direction | smallint | Evet |  | Hayir |  |  |
| DataCorrectionType | smallint | Evet |  | Hayir |  |  |
| RevisionAt | datetime2(7) | Evet |  | Hayir |  |  |
| RevisionDate | datetime2(7) | Evet |  | Hayir |  |  |
| DescriptionOld | nvarchar(4000) | Evet |  | Hayir |  |  |
| OtherPrice | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.Contracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractNo | nvarchar(450) | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| GroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ReelProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServicePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| CashRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  |  |
| FinanceControllerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FinanceControllerDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| IsJoker | bit | Hayir |  | Hayir |  |  |
| DeliveryMonth | int | Evet |  | Hayir |  |  |
| ScheduledDeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| FinanceDeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| ReelDeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeliveryStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeliveryEndDate | datetime2(7) | Evet |  | Hayir |  |  |
| FinanceDeliveryControllerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FinanceDeliveryControllerDate | datetime2(7) | Evet |  | Hayir |  |  |
| OperationDeliveryControllerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OperationDeliveryControllerDate | datetime2(7) | Evet |  | Hayir |  |  |
| CancellationReason | nvarchar(100) | Evet |  | Hayir |  |  |
| CompletionReason | nvarchar(4000) | Evet |  | Hayir |  |  |
| ServiceMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductMonthlyPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeliveryFirstInstallment | int | Hayir |  | Hayir |  |  |
| DeliveryLastInstallment | int | Hayir |  | Hayir |  |  |
| DeliveryFirstInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| DeliveryLastInstallmentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Guarantor1Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Guarantor1Tckno | nvarchar(20) | Evet |  | Hayir |  |  |
| Guarantor1Phone | nvarchar(20) | Evet |  | Hayir |  |  |
| Guarantor1Address | nvarchar(500) | Evet |  | Hayir |  |  |
| Guarantor2Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Guarantor2Tckno | nvarchar(20) | Evet |  | Hayir |  |  |
| Guarantor2Phone | nvarchar(20) | Evet |  | Hayir |  |  |
| Guarantor2Address | nvarchar(500) | Evet |  | Hayir |  |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ContractInput | varchar(max) | Evet |  | Hayir |  |  |
| ContractOutput | varchar(max) | Evet |  | Hayir |  |  |
| ContractProduct | varchar(max) | Evet |  | Hayir |  |  |
| IsOperationApproval | bit | Hayir | ((0)) | Hayir |  |  |
| IsInvoice | bit | Hayir | ((0)) | Hayir |  |  |
| RelatedContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  |  |
| ServicePriceLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateLast | decimal(18,2) | Evet |  | Hayir |  |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DelayingDeliveryMonth | int | Hayir | ((0)) | Hayir |  |  |
| PriceDiff | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| OldGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PassiveDegree | int | Hayir | ((0)) | Hayir |  |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  |  |
| ServiceFirstInstallmentPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| InstallmentPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ExpertiseDate | datetime2(7) | Evet |  | Hayir |  |  |
| ExpertisePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| IsExpertise | bit | Hayir | ((0)) | Hayir |  |  |
| IBAN | nvarchar(150) | Evet |  | Hayir |  |  |
| InvoiceDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeedDelivered | bit | Evet |  | Hayir |  |  |
| FirstPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FirstPortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FirstOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PremiumPayment | bit | Evet |  | Hayir |  |  |
| BidUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FolderNo | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| InvoiceNo | nvarchar(30) | Evet |  | Hayir |  |  |
| CustomerName | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerSurname | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerTckno | nvarchar(20) | Evet |  | Hayir |  |  |
| CustomerNo | nvarchar(100) | Evet |  | Hayir |  |  |
| GroupName | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerCity | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerTown | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerHomeTown | nvarchar(100) | Evet |  | Hayir |  |  |
| ProductName | nvarchar(100) | Evet |  | Hayir |  |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  |  |
| FinanceControllerName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioCode | nvarchar(50) | Evet |  | Hayir |  |  |
| PortfolioOwner | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioOrganizationName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioOrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioParentOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioParentOrganizationName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioParentOrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerSource | nvarchar(50) | Evet |  | Hayir |  |  |
| ServicePricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| CashPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| InstallmentPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| BillPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| IsPaid | bit | Evet |  | Hayir |  |  |
| ColorType | int | Evet |  | Hayir |  |  |
| InstallmentAmount | nvarchar(50) | Evet |  | Hayir |  |  |
| PaidInstallmentAmount | nvarchar(50) | Evet |  | Hayir |  |  |
| RemainingInstallmentAmount | nvarchar(50) | Evet |  | Hayir |  |  |
| CustomerPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerPortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsPendingActivity | bit | Evet |  | Hayir |  |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  |  |
| CreatedByUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerCityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerTownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerHomeTownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsDistance | bit | Evet |  | Hayir |  |  |
| IsJoinJob | bit | Hayir | ((1)) | Hayir |  |  |
| DelayedInstallmentCount | int | Evet |  | Hayir |  |  |
| ReturnPaymentStatus | tinyint | Evet |  | Hayir |  |  |
| SoundRecord | nvarchar(100) | Evet |  | Hayir |  |  |
| IsTradesman | bit | Evet |  | Hayir |  |  |
| GuaranteedBillGiven | bit | Evet |  | Hayir |  |  |
| GuaranteedBillReceived | bit | Evet |  | Hayir |  |  |
| LoadedBill | nvarchar(150) | Evet |  | Hayir |  |  |
| GuaranteedBillAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateWithOutCashPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| CustomerTaxNo | nvarchar(10) | Evet |  | Hayir |  |  |
| TaxNo | varchar(10) | Evet |  | Hayir |  |  |
| CustomerTaxOffice | varchar(100) | Evet |  | Hayir |  |  |
| OffsetContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OffsetGiroProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetGiroServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetContractOffsetLogUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewContractOffsetLogUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CancellationDate | datetime2(7) | Evet |  | Hayir |  |  |
| DidBillsCome | bit | Evet | ((0)) | Hayir |  |  |
| ReturnDescription | varchar(100) | Evet |  | Hayir |  |  |
| ReturnType | varchar(5) | Evet |  | Hayir |  |  |
| ReturnPetitionDate | datetime2(7) | Evet |  | Hayir |  |  |
| ReturnTransactionDate | datetime2(7) | Evet |  | Hayir |  |  |
| ReturnDate | datetime2(7) | Evet |  | Hayir |  |  |
| CarNumberPlate | varchar(50) | Evet |  | Hayir |  |  |
| ExpertiseValue | decimal(18,2) | Evet |  | Hayir |  |  |
| DeprivationOfRight | bit | Evet |  | Hayir |  |  |
| BillNo | varchar(50) | Evet |  | Hayir |  |  |
| DeliveryStatus | nvarchar(10) | Evet |  | Hayir |  |  |
| DeliveryDescription | nvarchar(1000) | Evet |  | Hayir |  |  |
| DeliveryAppointmentDate | datetime2(7) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MeskenContractNo | varchar(50) | Evet |  | Hayir |  |  |
| FirstProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| InflationIncreaseCount | int | Evet |  | Hayir |  |  |
| LegalPursuit | bit | Evet |  | Hayir |  |  |
| ReturnComplete | bit | Evet |  | Hayir |  |  |
| OffsetDelayingDeliveryMonth | int | Evet |  | Hayir |  |  |
| TransferDelayingDeliveryMonth | int | Evet |  | Hayir |  |  |
| ProductModel | char(3) | Evet |  | Hayir |  |  |
| InterimPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| InterimPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| CustomerPhone | varchar(50) | Evet |  | Hayir |  |  |
| SubStatus | smallint | Evet |  | Hayir |  |  |
| DepositDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeliveredProductType | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractLeavingUid | uniqueidentifier | Evet |  | Hayir |  |  |
| StatusReasonType | varchar(5) | Evet |  | Hayir |  |  |
| ManuelReconciliation | nvarchar(50) | Evet |  | Hayir |  |  |
| InsuranceDeductedDeliveryPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| DidPledgeAgreementCome | bit | Hayir | ((0)) | Hayir |  |  |
| HasVPInstallment | bit | Evet | ((0)) | Hayir |  |  |
| CanPayServicePriceInstbyVP | bit | Evet | ((0)) | Hayir |  |  |
| ContractProcess | smallint | Evet |  | Hayir |  |  |
| DeliveryDocumentsDeadlineDate | datetime2(7) | Evet |  | Hayir |  |  |
| LogoTransferStatus | smallint | Hayir | ((0)) | Hayir |  |  |
| VPProductInstalmentCount | int | Evet |  | Hayir |  |  |
| PledgeFolderNo | varchar(50) | Evet |  | Hayir |  |  |
| InsurancePaymentMethod | nvarchar(50) | Evet |  | Hayir |  |  |
| ConvertToPoint | bit | Evet |  | Hayir |  |  |
| MortgageDocumentNo | nvarchar(50) | Evet |  | Hayir |  |  |
| MortgagesTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DidMortgageAgreementCome | bigint | Evet |  | Hayir |  |  |
| DeliveryBillsStatus | bit | Evet | ((0)) | Hayir |  |  |
| IsDigitalApproval | bit | Evet |  | Hayir |  |  |
| SendToMobileDate | datetime2(7) | Evet |  | Hayir |  |  |
| ContractApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| PreInformationApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| MobileApprovalSender | uniqueidentifier | Evet |  | Hayir |  |  |
| AuthorizationId | varchar(50) | Evet |  | Hayir |  |  |
| PersonalDataApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsStartBothInstallmentAndServiceFee | bit | Hayir | ((0)) | Hayir |  |  |
| SendToDeliveryDocumentApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| PreviousStatus | nvarchar(10) | Evet |  | Hayir |  |  |
| IsActiveDocumentIssues | bit | Hayir | ((0)) | Hayir |  |  |
| ServicePriceCreditCardPartialCashRatio | decimal(18,2) | Evet |  | Hayir |  |  |
| NFCResult | smallint | Evet |  | Hayir |  |  |
| SpecialProcces | bit | Hayir | ((0)) | Hayir |  |  |
| ScheduledDateChangeType | smallint | Evet |  | Hayir |  |  |

## Crm.ContractTemplate

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Evet |  | Hayir | Crm.Products.Uid |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  |  |
| Text | nvarchar(max) | Evet |  | Hayir |  |  |
| ServiceType | nvarchar(50) | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| ProductModel | nvarchar(50) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.ContractTemplateVariables

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.CostForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CostDate | datetime2(7) | Hayir |  | Hayir |  |  |
| TotalPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| PaidDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsTransfer | bit | Hayir |  | Hayir |  |  |
| Confirm | bit | Hayir |  | Hayir |  |  |
| File | nvarchar(100) | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| CostTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.CostTypes.Uid |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| Name | nvarchar(200) | Evet |  | Hayir |  |  |
| ManagerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CostBudgetType | smallint | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SubStatus | smallint | Evet |  | Hayir |  |  |
| ApproveDate | datetime2(7) | Evet |  | Hayir |  |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  |  |
| CancelDescription | nvarchar(4000) | Evet |  | Hayir |  |  |
| TotalRequestedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| TotalDifferencePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| FileBankReceipt | nvarchar(100) | Evet |  | Hayir |  |  |
| TotalPreRequestedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| TotalProcessedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| TotalPaidPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |
| CostNo | varchar(8) | Evet |  | Hayir |  |  |

## Crm.CostItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| CostDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| CostFormUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostForms.Uid |  |
| CostTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostTypes.Uid |  |
| ReceiptNo | nvarchar(100) | Evet |  | Hayir |  |  |
| TaxRate | decimal(18,2) | Evet |  | Hayir |  |  |
| DescriptionDetail | nvarchar(4000) | Evet |  | Hayir |  |  |
| File | nvarchar(100) | Evet |  | Hayir |  |  |
| RequestedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| AdvanceDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsFirstItem | bit | Evet |  | Hayir |  |  |
| ProcessedPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.Costs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| CostTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.CostTypes.Uid |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| ExecutionMonth | int | Hayir |  | Hayir |  |  |
| ExecutionYear | int | Hayir |  | Hayir |  |  |
| Note | nvarchar(500) | Evet |  | Hayir |  |  |
| InvoiceType | nvarchar(50) | Evet |  | Hayir |  |  |
| InvoiceNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| InvoiceDate | datetime2(7) | Evet |  | Hayir |  |  |
| Count | int | Evet |  | Hayir |  |  |
| VAT | decimal(18,0) | Evet |  | Hayir |  |  |

## Crm.CostTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| IsCost | bit | Hayir | ((0)) | Hayir |  |  |
| Text | nvarchar(500) | Evet |  | Hayir |  |  |
| CostBudgetType | smallint | Evet |  | Hayir |  |  |

## Crm.CustomerLoginFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.CustomerLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  |  |
| DeviceId | varchar(200) | Evet |  | Hayir |  |  |
| Text | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.CustomerLoginSmsFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SmsPassword | nvarchar(100) | Evet |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| InstalledFrom | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.Customers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  |  |
| Tckno | nvarchar(11) | Evet |  | Hayir |  |  |
| CustomerNo | nvarchar(50) | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| EMail | nvarchar(100) | Evet |  | Hayir |  |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Address | nvarchar(500) | Evet |  | Hayir |  |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MaritalStatus | nvarchar(1) | Evet |  | Hayir |  |  |
| Gender | nvarchar(1) | Evet |  | Hayir |  |  |
| BirthDate | datetime2(7) | Evet |  | Hayir |  |  |
| PartnerName | nvarchar(100) | Evet |  | Hayir |  |  |
| PartnerPhone | nvarchar(50) | Evet |  | Hayir |  |  |
| ChildrenCount | int | Hayir |  | Hayir |  |  |
| HomePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| EMail2 | nvarchar(100) | Evet |  | Hayir |  |  |
| IsMember | bit | Hayir |  | Hayir |  |  |
| IsJoker | bit | Hayir |  | Hayir |  |  |
| IsNotCallMe | bit | Hayir |  | Hayir |  |  |
| IsLogo | bit | Hayir | ((0)) | Hayir |  |  |
| ContactChannel | nvarchar(50) | Evet |  | Hayir |  |  |
| Source | nvarchar(50) | Evet |  | Hayir |  |  |
| Category | nvarchar(50) | Evet |  | Hayir |  |  |
| OfficePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| OfficeAddress | nvarchar(500) | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| ReferanceUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| LogoID | int | Evet |  | Hayir |  |  |
| Password | nvarchar(50) | Evet |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TaxNo | nvarchar(10) | Evet |  | Hayir |  |  |
| CustomerTaxNo | varchar(10) | Evet |  | Hayir |  |  |
| TaxOffice | nvarchar(50) | Evet |  | Hayir |  |  |
| IsInAutomation | bit | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| LastMoveMesken | bit | Evet |  | Hayir |  |  |
| HasComplaint | bit | Evet |  | Hayir |  |  |
| LastTalkDate | datetime2(7) | Evet |  | Hayir |  |  |
| Param01 | bit | Evet |  | Hayir |  |  |
| CanPayByVP | bit | Hayir | ((1)) | Hayir |  |  |
| NationalityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerType | smallint | Evet |  | Hayir |  |  |
| FatherName | nvarchar(50) | Evet |  | Hayir |  |  |
| MotherName | nvarchar(50) | Evet |  | Hayir |  |  |
| BirthPlace | nvarchar(50) | Evet |  | Hayir |  |  |
| VerificationMethod | smallint | Evet |  | Hayir |  |  |
| NaceCode | nvarchar(10) | Evet |  | Hayir |  |  |
| IsMFAEnabled | bit | Evet |  | Hayir |  |  |
| IdentitySerialNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| IdentityExpirationDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.CustomerSources

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| IsLeadRequired | bit | Hayir | ((0)) | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| IsBranch | bit | Hayir | ((1)) | Hayir |  |  |
| IsMarketing | bit | Hayir | ((0)) | Hayir |  |  |
| UtmSources | nvarchar(200) | Evet |  | Hayir |  |  |
| IsDigital | bit | Hayir | ((0)) | Hayir |  |  |
| IsActive | bit | Hayir | ((1)) | Hayir |  |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  |  |
| IysSource | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.DailyServicePricePaidLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| InstallmentUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProcessDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Type | nvarchar(5) | Evet |  | Hayir |  |  |

## Crm.DataAnalysisLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Code | nvarchar(100) | Evet |  | Hayir |  |  |
| IsConfirmed | bit | Evet | ((0)) | Hayir |  |  |

## Crm.Debits

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DebitFile | nvarchar(100) | Evet |  | Hayir |  |  |
| Status | nvarchar(100) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  |  |
| Note | nvarchar(1000) | Evet |  | Hayir |  |  |
| InventoryUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.Deliveries

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| CostInclusive | bit | Hayir |  | Hayir |  |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid |  |
| AssurancePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ExpertizePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| DeliveryAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| DeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| FinancialDeliveryDate | datetime2(7) | Evet |  | Hayir |  |  |
| PaperWorkCompleteDate | datetime2(7) | Evet |  | Hayir |  |  |
| OffsettingContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| ProductType | nvarchar(max) | Evet |  | Hayir |  |  |
| IsComplete | bit | Hayir |  | Hayir |  |  |
| Receipt | varchar(100) | Evet |  | Hayir |  |  |

## Crm.DeliveryCallHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DeliveryCallUid | uniqueidentifier | Hayir |  | Hayir | Crm.DeliveryCalls.Uid |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OutBoundCallUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CallCount | int | Hayir | ((0)) | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| RecallDate | datetime2(7) | Evet |  | Hayir |  |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  |  |
| UnReachedDate | datetime2(7) | Evet |  | Hayir |  |  |
| OldValue | nvarchar(max) | Evet |  | Hayir |  |  |
| NewValue | nvarchar(max) | Evet |  | Hayir |  |  |
| TransactionName | nvarchar(100) | Evet |  | Hayir |  |  |
| OldValueText | nvarchar(100) | Evet |  | Hayir |  |  |
| NewValueText | nvarchar(100) | Evet |  | Hayir |  |  |
| FieldNameText | nvarchar(100) | Evet |  | Hayir |  |  |
| DocumentRequestedDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.DeliveryCallNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DeliveryCallUid | uniqueidentifier | Hayir |  | Hayir | Crm.DeliveryCalls.Uid |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| NoteText | nvarchar(max) | Evet |  | Hayir |  |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.DeliveryCalls

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OutBoundCallUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CallCount | int | Hayir | ((0)) | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| RecallDate | datetime2(7) | Evet |  | Hayir |  |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  |  |
| UnReachedDate | datetime2(7) | Evet |  | Hayir |  |  |
| DocumentRequestedDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.DeliveryDocumentApprovals

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| FileTypeUid | uniqueidentifier | Hayir |  | Hayir | Crm.FileTypes.Uid |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| OldStatus | smallint | Evet |  | Hayir |  |  |
| Comment | nvarchar(max) | Evet |  | Hayir |  |  |
| IsRequired | bit | Hayir | ((1)) | Hayir |  |  |
| ProductType | nvarchar(2) | Hayir |  | Hayir |  |  |
| ControlAt | datetime2(7) | Evet |  | Hayir |  |  |
| ControlBy | uniqueidentifier | Evet |  | Hayir |  |  |
| SendApprovalBy | uniqueidentifier | Evet |  | Hayir |  |  |
| GuarontorName | nvarchar(200) | Evet |  | Hayir |  |  |

## Crm.DeliveryEmployees

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| DayOfWeek | int | Evet |  | Hayir |  |  |

## Crm.DeliveryFiles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| DeliveryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| FileTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.FileTypes.Uid |  |
| FileUid | uniqueidentifier | Evet |  | Hayir | Crm.Files.Uid |  |
| GuarantorUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |

## Crm.DeliveryPaymentLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LogType | smallint | Evet |  | Hayir |  |  |
| Department | nvarchar(100) | Evet |  | Hayir |  |  |
| DeliveryPaymentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.DeliveryPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid |  |
| DeliveryAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| ProductType | nvarchar(10) | Evet |  | Hayir |  |  |
| InsuranceDeduction | decimal(18,2) | Evet |  | Hayir |  |  |
| CompletedDeliveryAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| BeforeDeliveryStatus | nvarchar(50) | Hayir |  | Hayir |  |  |
| BeforeDeliverySubStatus | smallint | Evet |  | Hayir |  |  |
| DeliveryRefundLogoManualAction | bit | Evet |  | Hayir |  |  |
| RefundAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| DeliveryApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| DeliveryRefundDate | datetime2(7) | Evet |  | Hayir |  |  |
| LogoNo | bigint | Evet |  | Hayir |  |  |
| LogoProcessDate | datetime | Evet |  | Hayir |  |  |
| BankUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BankAccountUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| Message | varchar(max) | Evet |  | Hayir |  |  |
| AccountList | varchar(max) | Evet |  | Hayir |  |  |
| ErrorList | varchar(max) | Evet |  | Hayir |  |  |
| DeliveryApporovalUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Notes | varchar(max) | Evet |  | Hayir |  |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  |  |
| PaymentUserUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.DeliveryRanges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid |  |
| StartMonth | int | Hayir |  | Hayir |  |  |
| EndMonth | int | Hayir |  | Hayir |  |  |
| StartMonthNotCampaign | int | Hayir | ((0)) | Hayir |  |  |
| EndMonthNotCampaign | int | Hayir | ((0)) | Hayir |  |  |
| StartRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| EndRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.DeliveryWorkAdvances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  |  |
| EndingAmount | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.DeprivationInqueries

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| PlateNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| RegistrationSerialNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| AsbisRegistrationReferenceNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| VehicleType | int | Evet |  | Hayir |  |  |
| VehicleBrand | nvarchar(50) | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| RegistrationStatus | bit | Hayir |  | Hayir |  |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  |  |
| ReasonType | smallint | Evet |  | Hayir |  |  |

## Crm.Distraints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DistraintOffice | nvarchar(200) | Evet |  | Hayir |  |  |
| FileNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| RenewalDate | datetime2(7) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.DocumentReads

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DocumentUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AllOrganitionRead | bit | Hayir | ((0)) | Hayir |  |  |
| AllRegionsRead | bit | Hayir | ((0)) | Hayir |  |  |

## Crm.Documents

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ImportUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Order | int | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.DrawCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid |  |
| DrawUid | uniqueidentifier | Evet |  | Hayir | Crm.Draws.Uid |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |

## Crm.Draws

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Message | nvarchar(4000) | Evet |  | Hayir |  |  |
| CodeLength | int | Hayir |  | Hayir |  |  |
| IsAppointment | bit | Hayir |  | Hayir |  |  |
| AppointmentCodeCount | int | Hayir |  | Hayir |  |  |
| IsContract | bit | Hayir |  | Hayir |  |  |
| ContractCodeCount | int | Hayir |  | Hayir |  |  |
| IsCandidate | bit | Hayir |  | Hayir |  |  |
| CandidateCodeCount | int | Hayir |  | Hayir |  |  |
| CodeMessage | nvarchar(4000) | Evet |  | Hayir |  |  |
| ContractMessage | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.ETesisTerkinContractIbans

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ETesisTerkinIntegrationUid | uniqueidentifier | Hayir |  | Hayir | Crm.ETesisTerkinIntegrations.Uid |  |
| ContractIBANUid | uniqueidentifier | Hayir |  | Hayir | Crm.ContractIBANs.Uid |  |

## Crm.ETesisTerkinIntegrations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgageUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| IntegrationNo | nvarchar(450) | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Customers.Uid |  |
| InsuranceUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ImmovableCityId | int | Hayir |  | Hayir |  |  |
| ImmovableTownId | int | Hayir |  | Hayir |  |  |
| ImmovableHomeTownId | int | Hayir |  | Hayir |  |  |
| ImmovableBlock | nvarchar(255) | Hayir |  | Hayir |  |  |
| ImmovableParcel | nvarchar(255) | Hayir |  | Hayir |  |  |
| IndependentUnitNo | nvarchar(255) | Hayir |  | Hayir |  |  |
| LandOffice | nvarchar(255) | Evet |  | Hayir |  |  |
| DocumentNumber | nvarchar(255) | Evet |  | Hayir |  |  |
| LandOfficeId | int | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| WageDate | datetime2(7) | Evet |  | Hayir |  |  |
| WageNumber | varchar(50) | Evet |  | Hayir |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| MortgagePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| MortgageFileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OfficialDeedFileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CancelDescription | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.Files

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| Link | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| DistraintUid | uniqueidentifier | Evet |  | Hayir | Crm.Distraints.Uid |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid |  |
| InventoryUid | uniqueidentifier | Evet |  | Hayir | Crm.Inventories.Uid |  |
| FileTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeliveryHistoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |
| DeliveryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| GuarantorUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeliveryFileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| CandidateUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MortgageInsuranceUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |
| TransferStatus | smallint | Evet | ((0)) | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApproveAt | datetime2(7) | Evet |  | Hayir |  |  |
| RejectAt | datetime2(7) | Evet |  | Hayir |  |  |
| RejectUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Path | nvarchar(400) | Evet |  | Hayir |  |  |
| ComplaintUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ComplaintNoteUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TicketUid | nvarchar(100) | Evet |  | Hayir |  |  |
| Hash | varchar(400) | Evet |  | Hayir |  |  |
| AuthorizationId | varchar(400) | Evet |  | Hayir |  |  |
| Fingerprint | nvarchar(400) | Evet |  | Hayir |  |  |

## Crm.FileTypeCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(4) | Evet |  | Hayir |  |  |
| OrderBy | int | Evet |  | Hayir |  |  |

## Crm.FileTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(max) | Evet |  | Hayir |  |  |
| Type | nvarchar(4) | Evet |  | Hayir |  |  |
| IsRequired | bit | Hayir |  | Hayir |  |  |
| Department | nvarchar(4) | Evet |  | Hayir |  |  |
| OrderBy | int | Evet |  | Hayir |  |  |
| IsTradesman | bit | Evet |  | Hayir |  |  |
| IsGuarantor | bit | Evet |  | Hayir |  |  |
| IsDelivery | bit | Evet |  | Hayir |  |  |
| ProductType | nvarchar(2) | Evet |  | Hayir |  |  |
| CategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsLegalProceeding | bit | Evet |  | Hayir |  |  |
| Path | varchar(300) | Evet |  | Hayir |  |  |
| NewPath | varchar(300) | Evet |  | Hayir |  |  |
| TransferStatus | smallint | Hayir | ((0)) | Hayir |  |  |

## Crm.Firms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| DefaultGroupStartDay | int | Hayir |  | Hayir |  |  |

## Crm.GroupProducts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.Groups.Uid |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid |  |

## Crm.Groups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| GroupDate | datetime2(7) | Hayir |  | Hayir |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |
| ClosedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| InstallmentCount | int | Evet |  | Hayir |  |  |
| LimitedProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| IsPool | bit | Hayir | ((0)) | Hayir |  |  |

## Crm.GroupsForBulkDrawQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| NotaryName | nvarchar(400) | Hayir |  | Hayir |  |  |
| OrganizationPlace | nvarchar(1000) | Hayir |  | Hayir |  |  |
| OrganizationDate | datetime2(7) | Hayir |  | Hayir |  |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |
| BallCount | int | Hayir | ((0)) | Hayir |  |  |
| Message | nvarchar(1000) | Evet |  | Hayir |  |  |

## Crm.Guarantors

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Tckno | nvarchar(20) | Evet |  | Hayir |  |  |
| Phone | nvarchar(20) | Evet |  | Hayir |  |  |
| Address | nvarchar(500) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| Number | int | Evet |  | Hayir |  |  |
| IsTradesman | bit | Evet |  | Hayir |  |  |

## Crm.Holidays

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Evet |  | Hayir |  |  |
| Name | varchar(50) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| Total | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.Installments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ContractRevisionUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| InstallmentNumber | int | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Status | nvarchar(100) | Evet |  | Hayir |  |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| PricePaid | decimal(18,2) | Hayir |  | Hayir |  |  |
| DueDate | datetime2(7) | Hayir |  | Hayir |  |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  |  |
| VariableIndexUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsLogo | bit | Hayir | ((0)) | Hayir |  |  |
| IsLast | bit | Hayir | ((0)) | Hayir |  |  |
| SentCountSMS | int | Hayir | ((0)) | Hayir |  |  |
| PostponePrice | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| PostponePricePaid | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| BankLogUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DidBillSend | bit | Evet |  | Hayir |  |  |
| ProcessDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| Sub_Type | nvarchar(10) | Evet |  | Hayir |  |  |
| Sub_InstallmentNumber | int | Evet |  | Hayir |  |  |
| PromissoryNotePostingDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.IntegrationApiLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| JsonData | nvarchar(1000) | Evet |  | Hayir |  |  |
| Result | nvarchar(2500) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.IntegrationApiLogs250919

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| JsonData | nvarchar(max) | Evet |  | Hayir |  |  |
| Result | nvarchar(2000) | Evet |  | Hayir |  |  |

## Crm.InternalFiles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir | (getdate()) | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| Link | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| InternalFileTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RejectUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Status | varchar(2) | Evet |  | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.InternalFileTypeCategories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(5) | Evet |  | Hayir |  |  |

## Crm.InternalFileTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(max) | Evet |  | Hayir |  |  |
| Type | nvarchar(4) | Evet |  | Hayir |  |  |
| IsRequired | bit | Hayir |  | Hayir |  |  |
| Department | nvarchar(4) | Evet |  | Hayir |  |  |
| OrderBy | int | Evet |  | Hayir |  |  |
| ProductType | nvarchar(2) | Evet |  | Hayir |  |  |
| CategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Path | varchar(250) | Evet |  | Hayir |  |  |

## Crm.InternetSubeLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.Inventories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Code | bigint | Hayir |  | Hayir |  | Identity |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| InventoryTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.InventoryTypes.Uid |  |
| DateOfPurchase | datetime2(7) | Hayir |  | Hayir |  |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| BuyCompany | nvarchar(1000) | Evet |  | Hayir |  |  |
| InvoiceFile | nvarchar(1000) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Brand | nvarchar(1000) | Evet |  | Hayir |  |  |
| Model | nvarchar(500) | Evet |  | Hayir |  |  |
| SerialNumber | nvarchar(400) | Evet |  | Hayir |  |  |
| Json | nvarchar(4000) | Evet |  | Hayir |  |  |
| AssetTag | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.InventoryDebits

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DebitUid | uniqueidentifier | Evet |  | Hayir | Crm.Debits.Uid |  |
| InventoryUid | uniqueidentifier | Evet |  | Hayir | Crm.Inventories.Uid |  |

## Crm.InventoryTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Properties | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.InvoiceLogoLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| CustomerNo | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractNo | nvarchar(50) | Evet |  | Hayir |  |  |
| InvoiceRef | nvarchar(200) | Evet |  | Hayir |  |  |
| InvoiceAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| BsmvAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| BsmvRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| InvoiceNo | varchar(50) | Evet |  | Hayir |  |  |
| BsmvCode | varchar(100) | Evet |  | Hayir |  |  |
| Status | smallint | Hayir | ((0)) | Hayir |  |  |
| InvoiceServiceCode | varchar(100) | Evet |  | Hayir |  |  |
| Message | varchar(max) | Evet |  | Hayir |  |  |

## Crm.IssueHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| DirectUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  |  |
| DirectDescription | nvarchar(max) | Evet |  | Hayir |  |  |
| Subject | nvarchar(max) | Evet |  | Hayir |  |  |
| Explanation | nvarchar(max) | Evet |  | Hayir |  |  |
| IsAnswer | bit | Evet |  | Hayir |  |  |
| Answer | nvarchar(max) | Evet |  | Hayir |  |  |
| AnswerBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| Status | nvarchar(max) | Evet |  | Hayir |  |  |
| IssueUid | uniqueidentifier | Evet |  | Hayir | Crm.Issues.Uid |  |

## Crm.Issues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Code | nvarchar(max) | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| DirectUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DirectDate | datetime2(7) | Evet |  | Hayir |  |  |
| DirectDescription | nvarchar(max) | Evet |  | Hayir |  |  |
| Subject | nvarchar(max) | Evet |  | Hayir |  |  |
| Explanation | nvarchar(max) | Evet |  | Hayir |  |  |
| IsAnswer | bit | Evet |  | Hayir |  |  |
| Answer | nvarchar(max) | Evet |  | Hayir |  |  |
| AnswerBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| AnswerDate | datetime2(7) | Evet |  | Hayir |  |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| Status | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.ITSystemUserLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  |  |
| IsLdap | bit | Evet |  | Hayir |  |  |

## Crm.LeadForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ID | nvarchar(200) | Evet |  | Hayir |  |  |
| FormID | nvarchar(200) | Evet |  | Hayir |  |  |
| FormCreateDate | datetime2(7) | Hayir |  | Hayir |  |  |
| CampaignID | nvarchar(200) | Evet |  | Hayir |  |  |
| AdID | nvarchar(200) | Evet |  | Hayir |  |  |
| AdSetID | nvarchar(200) | Evet |  | Hayir |  |  |
| Platform | nvarchar(100) | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| Log | nvarchar(max) | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RecordType | nvarchar(1) | Evet |  | Hayir |  |  |
| InstallmentRange | nvarchar(50) | Evet |  | Hayir |  |  |
| PriceRange | nvarchar(50) | Evet |  | Hayir |  |  |
| FormUid | nvarchar(200) | Evet |  | Hayir |  |  |
| Note | nvarchar(4000) | Evet |  | Hayir |  |  |
| AdFormUid | uniqueidentifier | Evet |  | Hayir | Crm.AdForms.Uid |  |
| IsRecurring | bit | Hayir | ((0)) | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid |  |
| IsRecurringOld | bit | Evet |  | Hayir |  |  |
| IsDigitalRecurring | bit | Hayir | ((0)) | Hayir |  |  |
| MobilePhone2 | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.Leads

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| SurName | nvarchar(100) | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| Message | nvarchar(4000) | Evet |  | Hayir |  |  |
| Status | nvarchar(100) | Evet |  | Hayir |  |  |
| Source | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsContact | bit | Evet | ((1)) | Hayir |  |  |
| EMail | nvarchar(50) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| CancellationReason | nvarchar(50) | Evet |  | Hayir |  |  |
| WaitDate | datetime2(7) | Evet |  | Hayir |  |  |
| MemberDate | datetime2(7) | Evet |  | Hayir |  |  |
| CampaignUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CampaignItemUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CityUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MaritalStatus | nvarchar(50) | Evet |  | Hayir |  |  |
| Gender | nvarchar(50) | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ReferanceUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ConvertToCandidateDate | datetime2(7) | Evet |  | Hayir |  |  |
| ConvertToCandidateByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsCenter | bit | Hayir | ((0)) | Hayir |  |  |
| CallOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsAppointmentConvert | bit | Hayir | ((0)) | Hayir |  |  |
| ConvertType | nvarchar(50) | Evet |  | Hayir |  |  |
| IsPassive | bit | Hayir | ((0)) | Hayir |  |  |
| IsHomeCar | nvarchar(50) | Evet |  | Hayir |  |  |
| IsHomeCarManuel | bit | Hayir | ((0)) | Hayir |  |  |
| IsDontCall | bit | Hayir | ((0)) | Hayir |  |  |
| IsDontSms | bit | Hayir | ((0)) | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MobilePhone2 | nvarchar(50) | Evet |  | Hayir |  |  |
| MobilePhoneFormat | nvarchar(100) | Evet |  | Hayir |  |  |
| OwnerBrandEnvoyUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerBrandEnvoyPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BrandEnvoyDate | datetime | Evet |  | Hayir |  |  |
| BrandEnvoyCall | bit | Evet |  | Hayir |  |  |
| BrandEnvoyCallOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BrandEnvoyCallDate | datetime | Evet |  | Hayir |  |  |
| CountOfCallLead | int | Evet |  | Hayir |  |  |
| CountOfCallCandidate | int | Evet |  | Hayir |  |  |
| CreatedByUserOrganizationType | nvarchar(50) | Evet |  | Hayir |  |  |
| PortfolioOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioRegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsAppointment | bit | Evet |  | Hayir |  |  |
| IsPendingActivity | bit | Evet |  | Hayir |  |  |
| LastContactDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsRecentlyPassive | bit | Evet |  | Hayir |  |  |
| CountryName | nvarchar(100) | Evet |  | Hayir |  |  |
| CityName | nvarchar(100) | Evet |  | Hayir |  |  |
| TownName | nvarchar(100) | Evet |  | Hayir |  |  |
| HomeTownName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioCode | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| PortfolioOrganizationName | nvarchar(100) | Evet |  | Hayir |  |  |
| OccupationName | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerSourceName | nvarchar(100) | Evet |  | Hayir |  |  |
| CreatedByUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| UpdatedByUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| ConvertToCandidateByUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| CallOwnerName | nvarchar(100) | Evet |  | Hayir |  |  |
| CustomerSourceIsDigital | bit | Evet |  | Hayir |  |  |
| CustomerSourceIsMarketing | bit | Evet |  | Hayir |  |  |
| CustomerBirthDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsJoinJob | bit | Evet |  | Hayir |  |  |
| RepPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsDuplicateBrandEnvoyLead | bit | Evet |  | Hayir |  |  |
| LastTalkDate | datetime2(7) | Evet |  | Hayir |  |  |
| OwnerRepFamiliarity | nvarchar(5) | Evet |  | Hayir |  |  |
| IsInAutomation | bit | Evet |  | Hayir |  |  |
| SmsChaseDate | datetime2(7) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MeskenCustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AutomationListName | varchar(50) | Evet |  | Hayir |  |  |
| IysTransactionId | nvarchar(100) | Evet |  | Hayir |  |  |
| IysRequestId | nvarchar(100) | Evet |  | Hayir |  |  |
| IysSubRequestId | nvarchar(100) | Evet |  | Hayir |  |  |
| SaveAgainDate | datetime2(7) | Evet |  | Hayir |  |  |
| Tckno | varchar(50) | Evet |  | Hayir |  |  |
| TaxNo | varchar(50) | Evet |  | Hayir |  |  |
| TmsfFirmId | smallint | Evet |  | Hayir |  |  |
| Address | varchar(200) | Evet |  | Hayir |  |  |
| TMSFFirmIds | varchar(20) | Evet |  | Hayir |  |  |
| AutoPortfolioAssignment | bit | Hayir | ((0)) | Hayir |  |  |
| FULLNAME | computed |  |  | Hayir |  | Computed |
| HardDeleted | bit | Hayir | ((0)) | Hayir |  |  |
| CancellationedByUserName | nvarchar(100) | Evet |  | Hayir |  |  |
| CancellationedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| CancellationedAt | datetime2(7) | Evet |  | Hayir |  |  |
| IsDontEmail | bit | Evet |  | Hayir |  |  |
| ConvertToCancelByManuel | bit | Evet |  | Hayir |  |  |
| ConvertToCandidateByManuel | bit | Evet |  | Hayir |  |  |
| IsRecurring | bit | Evet |  | Hayir |  |  |
| CallCenterContactKey | varchar(4000) | Evet |  | Hayir |  |  |
| IsSmsVerified | bit | Evet |  | Hayir |  |  |
| CallCenterContactUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsClarification | bit | Evet |  | Hayir |  |  |
| ClarificationDate | datetime2(7) | Evet |  | Hayir |  |  |
| ConsentIp | nvarchar(100) | Evet |  | Hayir |  |  |
| ConsentVersion | nvarchar(100) | Evet |  | Hayir |  |  |
| IsConsent | bit | Evet |  | Hayir |  |  |
| ConsentDate | datetime2(7) | Evet |  | Hayir |  |  |
| ClarificationIp | nvarchar(100) | Evet |  | Hayir |  |  |
| ClarificationVersion | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.LoginFaileds

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| MachineName | nvarchar(100) | Evet |  | Hayir |  |  |
| Message | nvarchar(400) | Evet |  | Hayir |  |  |
| IsLdap | bit | Hayir |  | Hayir |  |  |
| Device | nvarchar(20) | Evet |  | Hayir |  |  |

## Crm.Logins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  |  |
| IsCrm | bit | Evet |  | Hayir |  |  |
| IsLdap | bit | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.LogoLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LOGICALREF | int | Hayir |  | Hayir |  |  |
| LINEEXP | nvarchar(200) | Evet |  | Hayir |  |  |
| TRANNO | nvarchar(200) | Evet |  | Hayir |  |  |
| ACCFICHEREF | int | Hayir |  | Hayir |  |  |
| GENEXP1 | nvarchar(200) | Evet |  | Hayir |  |  |
| AMOUNT | decimal(18,2) | Hayir |  | Hayir |  |  |
| CODE | nvarchar(50) | Evet |  | Hayir |  |  |
| CAPIBLOCK_CREADEDDATE | datetime2(7) | Hayir |  | Hayir |  |  |
| CAPIBLOCK_MODIFIEDDATE | datetime2(7) | Hayir |  | Hayir |  |  |
| TYPE | nvarchar(200) | Evet |  | Hayir |  |  |
| PAYMENT_DATE | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.LogoPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(200) | Evet |  | Hayir |  |  |
| LogicalRef | int | Hayir |  | Hayir |  |  |
| LineExp | nvarchar(200) | Evet |  | Hayir |  |  |
| TranNo | nvarchar(200) | Evet |  | Hayir |  |  |
| AccfichefRef | int | Hayir |  | Hayir |  |  |
| GenexP1 | nvarchar(200) | Evet |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |
| CapiBlock_CreatedDate | datetime2(7) | Hayir |  | Hayir |  |  |
| CapiBlock_ModifiedDate | datetime2(7) | Hayir |  | Hayir |  |  |
| PaymentDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.LogoServiceLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| PostData | nvarchar(max) | Evet |  | Hayir |  |  |
| GetData | nvarchar(max) | Evet |  | Hayir |  |  |
| ServiceUrl | nvarchar(max) | Evet |  | Hayir |  |  |
| IsSuccess | bit | Hayir |  | Hayir |  |  |

## Crm.ManuelLeadForCallCenterQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LeadUid | varchar(50) | Hayir |  | Hayir |  |  |
| Name | varchar(100) | Evet |  | Hayir |  |  |
| SurName | varchar(100) | Evet |  | Hayir |  |  |
| Email | varchar(100) | Evet |  | Hayir |  |  |
| MobilePhone | varchar(50) | Evet |  | Hayir |  |  |
| CampaignId | varchar(300) | Evet |  | Hayir |  |  |
| ManuelListName | varchar(300) | Evet |  | Hayir |  |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| Message | varchar(300) | Evet |  | Hayir |  |  |

## Crm.ManuelPaymentRequests

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Type | nvarchar(10) | Hayir |  | Hayir |  |  |
| Status | nvarchar(10) | Hayir |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  |  |
| ContractStatus  | nvarchar(10) | Evet |  | Hayir |  |  |
| TotalPaymentBeforeRequest | decimal(18,2) | Hayir |  | Hayir |  |  |
| Description | nvarchar(100) | Evet |  | Hayir |  |  |
| Year | int | Hayir |  | Hayir |  |  |
| Month | int | Hayir |  | Hayir |  |  |
| ParentRegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BranchUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApproverUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| RejectedUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RejectedDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.MobileApplicationConfigurations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Appkey | nvarchar(50) | Evet |  | Hayir |  |  |
| Value | nvarchar(max) | Evet |  | Hayir |  |  |
| Platform | smallint | Hayir |  | Hayir |  |  |
| ID | int | Hayir |  | Hayir |  |  |
| Description | nvarchar(400) | Evet |  | Hayir |  |  |

## Crm.MobileConfigurationSettings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| AppId | int | Hayir |  | Hayir |  |  |
| PlatformId | int | Hayir |  | Hayir |  |  |
| VersionNo | nvarchar(50) | Evet |  | Hayir |  |  |
| DownloadLink | nvarchar(250) | Evet |  | Hayir |  |  |
| WarningMessage | nvarchar(500) | Evet |  | Hayir |  |  |
| IsNative | bit | Hayir |  | Hayir |  |  |
| ForceUpdate | bit | Hayir |  | Hayir |  |  |
| Enabled | bit | Hayir |  | Hayir |  |  |
| ServiceUrl | nvarchar(250) | Evet |  | Hayir |  |  |
| StoreStatus | int | Evet |  | Hayir |  |  |

## Crm.MobilePhoneNumbers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Number | nvarchar(100) | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |

## Crm.ModuleAuths

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(200) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| ModuleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Modules.Uid |  |

## Crm.Modules

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(200) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.MortgageCosts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid |  |
| Description | varchar(250) | Evet |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |

## Crm.MortgageInsurances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Amount | decimal(18,2) | Evet |  | Hayir |  |  |
| FinalAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |
| Description | nvarchar(max) | Evet |  | Hayir |  |  |
| MortgageUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid |  |
| DidConsensusDone | bit | Evet | ((0)) | Hayir |  |  |
| InsurancePaymentMethod | nvarchar(50) | Evet |  | Hayir |  |  |
| RenewalsNumber | int | Hayir | ((0)) | Hayir |  |  |
| IsRenewed | bit | Hayir | ((0)) | Hayir |  |  |
| PolicyStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| PolicyEndDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsTraceable | bit | Hayir | ((1)) | Hayir |  |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PreviousInsuranceUID | uniqueidentifier | Evet |  | Hayir |  |  |
| InsurancePlace | smallint | Hayir | ((0)) | Hayir |  |  |
| PolicyNo | nvarchar(255) | Evet |  | Hayir |  |  |
| BuildingCollateralAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| PolicyCompanyUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.MortgageLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgageState | nvarchar(4000) | Evet |  | Hayir |  |  |
| MortgageUid | uniqueidentifier | Hayir |  | Hayir | Crm.Mortgages.Uid |  |
| IsMesken | bit | Evet |  | Hayir |  |  |

## Crm.MortgagePledgeConsents

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| PledgeUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |
| TCKN | varchar(50) | Evet |  | Hayir |  |  |
| TaxNumber | varchar(50) | Evet |  | Hayir |  |  |
| VehiclePlateNumber | varchar(50) | Evet |  | Hayir |  |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Hayir |  | Hayir |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |
| ConsentEGMRReferenceNo | bigint | Evet |  | Hayir |  |  |
| Description | varchar(400) | Evet |  | Hayir |  |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |
| Process | smallint | Hayir |  | Hayir |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |

## Crm.MortgagePledgeRemovals

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| PledgeUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |
| RemovalRequestDate | datetime2(7) | Evet |  | Hayir |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |
| RemovalReason | smallint | Evet |  | Hayir |  |  |

## Crm.MortgagePledges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| VehiclePlateNumber | varchar(50) | Evet |  | Hayir |  |  |
| VehicleRegistrationSerialNumber | varchar(100) | Evet |  | Hayir |  |  |
| VehicleAsbisRegistrationReferenceNumber | varchar(100) | Evet |  | Hayir |  |  |
| DocumentID | varchar(50) | Evet |  | Hayir |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |
| PledgeRequestDate | datetime2(7) | Evet |  | Hayir |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |
| VehicleRegistrationID | varchar(100) | Evet |  | Hayir |  |  |
| VehicleType | varchar(100) | Evet |  | Hayir |  |  |
| VehicleProblemStatus | int | Evet |  | Hayir |  |  |
| TNBEGMReferenceNo | varchar(100) | Evet |  | Hayir |  |  |
| TNBInsertSequence | int | Evet |  | Hayir |  |  |
| TNBInsertDate | datetime2(7) | Evet |  | Hayir |  |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |
| PledgeRemovalUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.MortgagePledgeVehicleBrandModels

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Hayir |  | Hayir |  |  |
| MortgagePledgeVehicleBrandUid | uniqueidentifier | Hayir |  | Hayir | Crm.MortgagePledgeVehicleBrands.Uid |  |

## Crm.MortgagePledgeVehicleBrands

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | varchar(50) | Hayir |  | Hayir |  |  |

## Crm.MortgagePledgeVehicleTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ID | int | Hayir |  | Hayir |  |  |
| Name | varchar(50) | Hayir |  | Hayir |  |  |
| Order | int | Hayir |  | Hayir |  | Identity |
| Code | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.MortgagePrePledges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Name | varchar(100) | Evet |  | Hayir |  |  |
| Surname | varchar(100) | Evet |  | Hayir |  |  |
| TCKN | varchar(50) | Evet |  | Hayir |  |  |
| FileNumber | varchar(150) | Evet |  | Hayir |  |  |
| EngineNumber | varchar(50) | Evet |  | Hayir |  |  |
| ChassisNumber | varchar(50) | Evet |  | Hayir |  |  |
| ModelYear | varchar(50) | Evet |  | Hayir |  |  |
| VehicleType | int | Evet |  | Hayir |  |  |
| VehicleBrand | varchar(100) | Evet |  | Hayir |  |  |
| PrePledgeRequestDate | datetime2(7) | Evet |  | Hayir |  |  |
| BankName | varchar(150) | Evet |  | Hayir |  |  |
| BankBranchName | varchar(250) | Evet |  | Hayir |  |  |
| BankBranchCode | int | Evet |  | Hayir |  |  |
| TNBEGMRReferenceNo | varchar(100) | Evet |  | Hayir |  |  |
| VehicleRegistrationSerialNumber | varchar(100) | Evet |  | Hayir |  |  |
| TNBInsertDate | datetime2(7) | Evet |  | Hayir |  |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| QueueStatus | smallint | Evet |  | Hayir |  |  |
| QueueSubStatus | smallint | Evet |  | Hayir |  |  |
| QueueMessage | varchar(max) | Evet |  | Hayir |  |  |
| QueueStatusConvertPledge | smallint | Evet |  | Hayir |  |  |
| QueueSubStatusConvertPledge | smallint | Evet |  | Hayir |  |  |
| QueueMessageConvertPledge | varchar(max) | Evet |  | Hayir |  |  |
| MortgagePledgeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgagePledges.Uid |  |
| VehicleBrandUid | uniqueidentifier | Evet |  | Hayir |  |  |
| VehicleModelUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TaxNo | nvarchar(10) | Evet |  | Hayir |  |  |

## Crm.Mortgages

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| Status | nvarchar(100) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| MortgageOffice | nvarchar(100) | Evet |  | Hayir |  |  |
| FileNumber | nvarchar(100) | Evet |  | Hayir |  |  |
| RenewalDate | datetime2(7) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| Price | decimal(18,2) | Evet |  | Hayir |  |  |
| IsPricePaid | bit | Hayir | ((0)) | Hayir |  |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Mortgages.Uid |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| NotaryOffice | nvarchar(100) | Evet |  | Hayir |  |  |
| WageNumber | nvarchar(50) | Evet |  | Hayir |  |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid |  |
| PledgeDate | datetime2(7) | Evet |  | Hayir |  |  |
| PricePaid | decimal(18,0) | Evet |  | Hayir |  |  |
| LandOffice | nvarchar(100) | Evet |  | Hayir |  |  |
| AmountOfBidBond | decimal(18,0) | Evet |  | Hayir |  |  |
| ReleaseDate | datetime2(7) | Evet |  | Hayir |  |  |
| LegalStatus | varchar(25) | Evet |  | Hayir |  |  |
| DepositAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| ClosedDate | datetime2(7) | Evet |  | Hayir |  |  |
| SubTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ActiveDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.MortgageTypes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(100) | Evet |  | Hayir |  |  |
| Fields | nvarchar(3000) | Evet |  | Hayir |  |  |
| Formula | nvarchar(200) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| IsPrivileged | bit | Evet |  | Hayir |  |  |
| canBeRenewed | bit | Evet |  | Hayir |  |  |
| ParentTypeUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Order | smallint | Evet |  | Hayir |  |  |

## Crm.NaceCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| NaceCode | nvarchar(10) | Hayir |  | Hayir |  |  |
| SectorCode | nvarchar(10) | Evet |  | Hayir |  |  |
| SectorDefinition | nvarchar(100) | Evet |  | Hayir |  |  |
| OccupationCode | nvarchar(10) | Evet |  | Hayir |  |  |
| OccupationDefinition | nvarchar(255) | Evet |  | Hayir |  |  |
| NaceDescription | nvarchar(4000) | Evet |  | Hayir |  |  |

## Crm.Nationalities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Code | nvarchar(20) | Evet |  | Hayir |  |  |

## Crm.NotaryLists

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| NotaryResultUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotaryResults.Uid |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| Month | int | Hayir |  | Hayir |  |  |
| IsSuccess | bit | Hayir |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| DrawOrderNo | int | Hayir | ((0)) | Hayir |  |  |

## Crm.NotaryResults

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.Groups.Uid |  |
| NotaryName | nvarchar(100) | Evet |  | Hayir |  |  |
| OrganizationDate | datetime2(7) | Hayir |  | Hayir |  |  |
| OrganizationPlace | nvarchar(100) | Evet |  | Hayir |  |  |
| NotaryFile | nvarchar(200) | Evet |  | Hayir |  |  |
| MinMonth | int | Hayir |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| ApproveControllerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| ApproveControllerDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| OldNotaryFile | nvarchar(200) | Evet |  | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |

## Crm.NotDeliveredOnDeliveryDates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| FinanceDeliveryDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ProductPriceWithInsuranceCuts | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.NotificationGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(max) | Evet |  | Hayir |  |  |
| Key | nvarchar(max) | Evet |  | Hayir |  |  |
| Description | nvarchar(150) | Evet |  | Hayir |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |
| Token | nvarchar(max) | Evet |  | Hayir |  |  |
| LastSendingDate | datetime2(7) | Evet |  | Hayir |  |  |
| TotalSendingCount | int | Hayir |  | Hayir |  |  |
| LastSenderUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| Title | nvarchar(max) | Evet |  | Hayir |  |  |
| ProcedureName | varchar(50) | Evet |  | Hayir |  |  |

## Crm.NotificationGroupSubscriber

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid |  |
| GroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotificationGroups.Uid |  |

## Crm.NotificationLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| NotificationGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.NotificationGroups.Uid |  |
| Title | nvarchar(max) | Evet |  | Hayir |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |
| ImageUrl | nvarchar(max) | Evet |  | Hayir |  |  |
| Data | nvarchar(max) | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.NotificationVariables

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Key | nvarchar(max) | Evet |  | Hayir |  |  |
| Name | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.Occupations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.OffsetLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OrganizationName | nvarchar(50) | Evet |  | Hayir |  |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RegionName | nvarchar(50) | Evet |  | Hayir |  |  |
| PetitionDate | datetime2(7) | Evet |  | Hayir |  |  |
| TransactionDate | datetime2(7) | Evet |  | Hayir |  |  |
| PortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioOwnerName | nvarchar(50) | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| OffsetContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OffsetContractNo | nvarchar(max) | Evet |  | Hayir |  |  |
| NewContractNo | nvarchar(10) | Evet |  | Hayir |  |  |
| OffsetProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OffsetProductName | nvarchar(150) | Evet |  | Hayir |  |  |
| NewProductName | nvarchar(150) | Evet |  | Hayir |  |  |
| OffsetContractCreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| NewContractCreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| OffsetIsDraw | bit | Hayir |  | Hayir |  |  |
| NewIsDraw | bit | Hayir |  | Hayir |  |  |
| IncrementRate | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewGroupName | nvarchar(50) | Evet |  | Hayir |  |  |
| OffsetServiceType | nvarchar(5) | Evet |  | Hayir |  |  |
| NewServiceType | nvarchar(5) | Evet |  | Hayir |  |  |
| OffsetProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| NewProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetRawServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| NewServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| Status | nvarchar(5) | Evet |  | Hayir |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |
| CustomerName | nvarchar(150) | Evet |  | Hayir |  |  |
| OffsetGroupName | nvarchar(max) | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| OffsetInstallmentCount | nvarchar(3) | Evet |  | Hayir |  |  |
| NewInstallmentCount | nvarchar(3) | Evet |  | Hayir |  |  |
| ProductPriceDifference | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDifference | decimal(18,2) | Evet |  | Hayir |  |  |
| NewContractStatus | nvarchar(3) | Evet |  | Hayir |  |  |
| NewPaidServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetPaidServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| NewTotalPaid | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetTotalPaid | decimal(18,2) | Evet |  | Hayir |  |  |
| NewServicePriceReflected | decimal(18,2) | Evet |  | Hayir |  |  |
| BidApprovalRole | varchar(5) | Evet |  | Hayir |  |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SubStatus | nvarchar(5) | Evet |  | Hayir |  |  |
| CompletedPriceDifference | decimal(18,2) | Evet |  | Hayir |  |  |
| OffsetContractServiceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| NewContractServiceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| IsContractRevisionDecrease | bit | Evet |  | Hayir |  |  |

## Crm.OffsetProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OffsetLogUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Department | uniqueidentifier | Evet |  | Hayir |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |
| OffsetProcessType | smallint | Hayir |  | Hayir |  |  |

## Crm.OnlineUsers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Token | uniqueidentifier | Evet |  | Hayir |  |  |
| ComputerName | nvarchar(max) | Evet |  | Hayir |  |  |
| Device | nvarchar(max) | Evet |  | Hayir |  |  |
| SysStartTime | datetime2(7) | Hayir | (sysutcdatetime()) | Hayir |  |  |
| SysEndTime | datetime2(7) | Hayir | (CONVERT([datetime2],'9999-12-31 23:59:59.9999999')) | Hayir |  |  |

## Crm.Opportunities

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| MinProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MaxProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MinCashPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MaxCashPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MinServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| MaxServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| InComeLevelOfMonth | nvarchar(50) | Evet |  | Hayir |  |  |
| MinMontlyAffordAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| MaxMontlyAffordAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| RentPriceOfMonth | decimal(18,2) | Evet |  | Hayir |  |  |
| IsTenant | bit | Hayir |  | Hayir |  |  |
| IsInterimPayment | bit | Hayir |  | Hayir |  |  |
| IsIncreasedInstallement | bit | Hayir |  | Hayir |  |  |
| IsServicePriceInstallement | bit | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| LeadUid | uniqueidentifier | Hayir |  | Hayir | Crm.Leads.Uid |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid |  |
| Temperature | int | Evet |  | Hayir |  |  |
| CustomerSourceUid | uniqueidentifier | Evet |  | Hayir | Crm.CustomerSources.Uid |  |
| CustomerUid1 | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| OccupationUid | uniqueidentifier | Evet |  | Hayir | Crm.Occupations.Uid |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.OrganizationAreas

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| AreaUid | uniqueidentifier | Hayir |  | Hayir | Crm.Areas.Uid |  |
| LastAssignment | datetime2(7) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.OrganizationHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.OrganizationMonthlyTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Period | datetime | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| Target | bigint | Hayir |  | Hayir |  |  |

## Crm.Organizations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| FirmUid | uniqueidentifier | Evet |  | Hayir | Crm.Firms.Uid |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| CountryUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| HomeTownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| Address | nvarchar(4000) | Evet |  | Hayir |  |  |
| MuhasebeCode | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| AddressDescription | nvarchar(4000) | Evet |  | Hayir |  |  |
| MapLink | nvarchar(200) | Evet |  | Hayir |  |  |
| PhotoLink | nvarchar(200) | Evet |  | Hayir |  |  |
| CostCode | nvarchar(100) | Evet |  | Hayir |  |  |
| LeadCount | int | Hayir | ((0)) | Hayir |  |  |
| OldLeadCount | int | Hayir | ((0)) | Hayir |  |  |
| BranchCategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Phone | nvarchar(50) | Evet |  | Hayir |  |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  |  |
| ManagerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| BankCode | nvarchar(50) | Evet |  | Hayir |  |  |
| Gl_Code349 | nvarchar(50) | Evet |  | Hayir |  |  |
| Gl_Code136 | nvarchar(50) | Evet |  | Hayir |  |  |
| NameForLogo | varchar(50) | Evet |  | Hayir |  |  |
| CostCodeForLogo | varchar(4) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsPassive | bit | Evet |  | Hayir |  |  |
| MonthlyBudgetAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| ADOrganizationalUnit | varchar(200) | Evet |  | Hayir |  |  |
| EnabledLdap | bit | Hayir | ((0)) | Hayir |  |  |
| EnabledKEPLastVersion | bit | Hayir | ((0)) | Hayir |  |  |
| BranchID | int | Evet |  | Hayir |  |  |
| AppleMapsLink | nvarchar(200) | Evet |  | Hayir |  |  |
| IsUsedForFeedback | bit | Evet |  | Hayir |  |  |
| Email | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.Performances

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| PerformanceDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Point | int | Hayir |  | Hayir |  |  |
| PhonePoint | int | Hayir |  | Hayir |  |  |
| AppointmentCount | int | Hayir |  | Hayir |  |  |
| AppointmentPoint | int | Hayir |  | Hayir |  |  |
| OutAppointmentCount | int | Hayir |  | Hayir |  |  |
| OutAppointmentPoint | int | Hayir |  | Hayir |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |
| ContractPoint | int | Hayir |  | Hayir |  |  |
| PhoneCount | int | Hayir |  | Hayir |  |  |

## Crm.PerformancesTemp

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| PerformanceDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Point | int | Hayir |  | Hayir |  |  |
| PhonePoint | int | Hayir |  | Hayir |  |  |
| AppointmentCount | int | Hayir |  | Hayir |  |  |
| AppointmentPoint | int | Hayir |  | Hayir |  |  |
| OutAppointmentCount | int | Hayir |  | Hayir |  |  |
| OutAppointmentPoint | int | Hayir |  | Hayir |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |
| ContractPoint | int | Hayir |  | Hayir |  |  |
| PhoneCount | int | Hayir |  | Hayir |  |  |

## Crm.PlannedPeriodicDeliveryAmounts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| PlannedAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| RealizedAmount | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.Portfolios

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| Code | nvarchar(100) | Evet |  | Hayir |  |  |
| LastAssignDate | datetime2(7) | Hayir |  | Hayir |  |  |
| IsActive | bit | Evet | ((1)) | Hayir |  |  |
| LastAssignBranchDate | datetime2(7) | Evet |  | Hayir |  |  |
| LastAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  |  |
| Type | varchar(50) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.PosPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| LineNo | int | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| BankUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| IsTransferred | bit | Hayir |  | Hayir |  |  |
| TransferDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.PostVirmanQueues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OldContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| OldCustomerUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| OldCustomerNo | nvarchar(450) | Hayir |  | Hayir |  |  |
| NewContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| NewCustomerUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| NewCustomerNo | nvarchar(450) | Hayir |  | Hayir |  |  |
| OldProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| NewProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| OldServicePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| NewServicePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| OldContractCreatedDate | datetime2(7) | Hayir |  | Hayir |  |  |
| NewContractCreatedDate | datetime2(7) | Hayir |  | Hayir |  |  |
| LogoProcessDate | datetime2(7) | Evet |  | Hayir |  |  |
| Type | nvarchar(10) | Evet |  | Hayir |  |  |
| TotalPaid | decimal(18,2) | Hayir |  | Hayir |  |  |
| RepPaymentPaid | decimal(18,2) | Hayir |  | Hayir |  |  |
| JsonContent | nvarchar(max) | Evet |  | Hayir |  |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| Message | nvarchar(400) | Evet |  | Hayir |  |  |

## Crm.PremiumBranchRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| BranchCategoryUid | uniqueidentifier | Hayir |  | Hayir | Crm.BranchCategories.Uid |  |
| Count | int | Hayir |  | Hayir |  |  |
| Target | decimal(18,2) | Hayir |  | Hayir |  |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  |  |
| ATarget | decimal(18,2) | Hayir |  | Hayir |  |  |
| ARate | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| SalesmanRate | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |

## Crm.PremiumContracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| PremiumUid | uniqueidentifier | Evet |  | Hayir | Crm.Premiums.Uid |  |
| PremiumTimingUid | uniqueidentifier | Evet |  | Hayir | Crm.PremiumTimings.Uid |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| FirstMultiplier | decimal(18,2) | Hayir |  | Hayir |  |  |
| Factor | decimal(18,2) | Hayir |  | Hayir |  |  |
| Bonus | decimal(18,2) | Hayir |  | Hayir |  |  |
| Performance | decimal(18,2) | Hayir |  | Hayir |  |  |
| DownPayment | decimal(18,2) | Hayir |  | Hayir |  |  |
| PaymentInDays | decimal(18,2) | Hayir |  | Hayir |  |  |
| PrimiumPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| BranchPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| IsInstallment | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.PremiumItems

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| PremiumUid | uniqueidentifier | Evet |  | Hayir | Crm.Premiums.Uid |  |
| PremiumContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumContracts.Uid |  |
| InstallmentUid | uniqueidentifier | Hayir |  | Hayir | Crm.Installments.Uid |  |
| Price | decimal(18,2) | Hayir |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| Type | int | Hayir |  | Hayir |  |  |
| PrimiumPrice | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| Bonus | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| BranchPrice | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| PerformancePrice | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |

## Crm.Premiums

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| Month | int | Hayir |  | Hayir |  |  |
| Year | int | Hayir |  | Hayir |  |  |
| BranchCategoryUid | uniqueidentifier | Hayir |  | Hayir | Crm.BranchCategories.Uid |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| CurrentPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| IsPaid | bit | Hayir |  | Hayir |  |  |
| Rates | nvarchar(4000) | Evet |  | Hayir |  |  |
| PremiumTimingGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumTimingGroups.Uid |  |
| PaidDate | datetime2(7) | Evet |  | Hayir |  |  |
| PremiumUserTypeRateUid | uniqueidentifier | Evet |  | Hayir | Crm.PremiumUserTypeRates.Uid |  |
| TotalPremium | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.PremiumTimingGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| IsNoneTiming | bit | Hayir |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.PremiumTimings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| PremiumTimingGroupUid | uniqueidentifier | Hayir |  | Hayir | Crm.PremiumTimingGroups.Uid |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid |  |
| IsPaid | bit | Hayir |  | Hayir |  |  |
| ARate | decimal(18,2) | Hayir |  | Hayir |  |  |
| BRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| CRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| DRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| TRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| PaymentInDays | int | Hayir |  | Hayir |  |  |
| PaymentInDaysRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| PerformanceRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| DownPaymentRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| BranchTargetRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| BranchATargetRate | decimal(18,2) | Hayir |  | Hayir |  |  |

## Crm.PremiumUserTypeRates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| Percent | int | Hayir |  | Hayir |  |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  |  |
| Scale | decimal(18,2) | Hayir |  | Hayir |  |  |
| Bonus | decimal(18,2) | Hayir |  | Hayir |  |  |

## Crm.Products

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| ServiceInstallmentCount | int | Hayir |  | Hayir |  |  |
| CashInstallmentCount | int | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Model | nvarchar(200) | Evet |  | Hayir |  |  |
| DeliveryMonth | int | Hayir |  | Hayir |  |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForBranch | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| ContractHtml | nvarchar(500) | Evet |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| FixedIndex | decimal(18,2) | Evet |  | Hayir |  |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.VariableIndexGroups.Uid |  |
| IncreaseRateAfterDelivery | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForBranchLast | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| ServiceRateForRegionLast | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| ServiceRateForGeneralManagerLast | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| IsServicePriceDivided | bit | Hayir | ((0)) | Hayir |  |  |
| ServiceRateForBranchFirst | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| ServiceRateForRegionFirst | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| ServiceRateForGeneralManagerFirst | decimal(18,2) | Evet | ((0)) | Hayir |  |  |
| IsServicePriceDividedUntilDelivery | bit | Hayir | ((0)) | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceChargedBeforeDelivery | bit | Hayir | ((0)) | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceDistributed | bit | Hayir | ((0)) | Hayir |  |  |
| ServicePriceDistributedRateForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLast | decimal(18,2) | Evet |  | Hayir |  |  |
| IncreaseRateAfterDeliveryArray | nvarchar(100) | Evet |  | Hayir |  |  |
| MinProductPriceForDistributed | decimal(18,2) | Evet |  | Hayir |  |  |
| MinProductPriceForDeliveryDistributed | decimal(18,2) | Evet |  | Hayir |  |  |
| PremiumRate | decimal(18,2) | Evet |  | Hayir |  |  |
| KayitVar | bit | Hayir | ((0)) | Hayir |  |  |
| FlexibleDeliveryRate | decimal(18,2) | Evet |  | Hayir |  |  |
| IncreaseRateBeforeDelivery | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| GroupLimit | int | Evet |  | Hayir |  |  |
| MaxProductPrice | decimal(18,0) | Evet |  | Hayir |  |  |
| MinProductPrice | decimal(18,0) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| DownPaymentUpperLimit | int | Evet |  | Hayir |  |  |
| ServicePriceLoweLimit | int | Evet |  | Hayir |  |  |
| FirstInstallmentRate | decimal(18,2) | Evet | ((1)) | Hayir |  |  |
| Featured | bit | Evet |  | Hayir |  |  |
| DistributedCashRate | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForCEO | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| ServiceRateForCEOLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForCEOFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| PointServiceRateLimit | decimal(18,2) | Evet |  | Hayir |  |  |
| CashPaymentType | varchar(2) | Evet |  | Hayir |  |  |
| IsCashPayment | bit | Evet |  | Hayir |  |  |
| IsServicePriceInstallment | bit | Evet |  | Hayir |  |  |
| ServiceFirstInstallmentRate | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentForGeneralManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceInstallmentCount | int | Evet |  | Hayir |  |  |
| ServicePriceCashPriceLimit | decimal(18,2) | Evet |  | Hayir |  |  |
| NoCashPaymentDiscount | bit | Evet |  | Hayir |  |  |
| AnnualRateOfIncrease | decimal(18,2) | Evet |  | Hayir |  |  |
| DiscountRate | decimal(18,2) | Evet |  | Hayir |  |  |
| ElasticRate | decimal(18,2) | Evet |  | Hayir |  |  |
| InterimPayment | int | Evet |  | Hayir |  |  |
| MaxInstallmentCount | int | Evet |  | Hayir |  |  |
| MinDeliveryMonth | int | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CashRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceDividedFifth | bit | Evet |  | Hayir |  |  |
| IsServicePriceDividedFourth | bit | Evet |  | Hayir |  |  |
| IsServicePriceDividedSecond | bit | Evet |  | Hayir |  |  |
| IsServicePriceDividedThird | bit | Evet |  | Hayir |  |  |
| PassiveDate | datetime2(7) | Evet |  | Hayir |  |  |
| ServicePriceChargedBeforeDeliveryRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDistributedRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDividedUntilDeliveryRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirstFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirstFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirstThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignFirstTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLastFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLastFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLastThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateDividedNotCampaignLastTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchFirstFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchFirstFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchFirstThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchFirstTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchLastFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchLastFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchLastThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchLastTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManager | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerFirstFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerFirstFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerFirstThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerFirstTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerLast | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerLastFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerLastFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerLastThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForBranchManagerLastTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerFirstFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerFirstFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerFirstThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerFirstTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerLastFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerLastFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerLastThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForGeneralManagerLastTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionFirstFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionFirstFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionFirstThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionFirstTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionLastFive | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionLastFour | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionLastThree | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateForRegionLastTwo | decimal(18,2) | Evet |  | Hayir |  |  |
| InflationRate | decimal(18,2) | Evet |  | Hayir |  |  |
| IsTmsf | bit | Hayir | ((0)) | Hayir |  |  |
| OldProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| HasLottery | bit | Evet |  | Hayir |  |  |
| InstallmentPriceMaxLimit | decimal(18,2) | Evet |  | Hayir |  |  |
| IsServicePriceCreditCardInstallment | bit | Evet |  | Hayir |  |  |
| ServicePriceCreditCardForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |
| IncreaseRateByMonth | int | Evet |  | Hayir |  |  |
| SixMonthsRateOfIncrease | decimal(18,2) | Evet |  | Hayir |  |  |
| IncreasePeriodMonth | int | Evet |  | Hayir |  |  |
| FirstServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |
| IsServicePriceCreditCardPartialInstallment | bit | Evet |  | Hayir |  |  |
| ServicePriceCreditCardPartialForBranch | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardPartialNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardPartialForRegion | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceCreditCardPartialForCEO | decimal(18,2) | Evet |  | Hayir |  |  |
| SpecialCashRateFirst | decimal(18,2) | Evet |  | Hayir |  |  |
| SpecialCashRateSecond | decimal(18,2) | Evet |  | Hayir |  |  |
| FragmentationServicePriceCreditCardMaxInstallmentCount | int | Evet |  | Hayir |  |  |
| PreventIncreaseAfterDelivery | bit | Hayir | ((0)) | Hayir |  |  |

## Crm.ProxyOrganizations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProxyUserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| ProxyStartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| ProxyEndDate | datetime2(7) | Hayir |  | Hayir |  |  |

## Crm.QualityAnswers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Point | int | Hayir |  | Hayir |  |  |
| QualityQuestionUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityQuestions.Uid |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |

## Crm.QualityForms

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |

## Crm.QualityNotes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Note | nvarchar(max) | Evet |  | Hayir |  |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid |  |

## Crm.QualityQuestions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Type | nvarchar(100) | Evet |  | Hayir |  |  |
| Order | int | Hayir |  | Hayir |  |  |
| Weight | int | Hayir |  | Hayir |  |  |
| Question | nvarchar(4000) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| QualityFormUid | uniqueidentifier | Evet |  | Hayir | Crm.QualityForms.Uid |  |
| UserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |

## Crm.RepCampaigns

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid |  |
| PeriodDate | datetime2(7) | Hayir |  | Hayir |  |  |
| AdviceCount | int | Hayir |  | Hayir |  |  |
| DrawNumber | int | Evet |  | Hayir |  |  |
| Winner | smallint | Evet |  | Hayir |  |  |

## Crm.RepContracts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| AllowanceYear | int | Evet |  | Hayir |  |  |
| AllowanceMonth | int | Evet |  | Hayir |  |  |

## Crm.RepGifts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| ImagePath | nvarchar(500) | Evet |  | Hayir |  |  |
| RequiredPoint | int | Hayir |  | Hayir |  |  |

## Crm.RepIbans

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid |  |
| Iban | nvarchar(50) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| BankCode | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.RepPaymentDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepPaymentUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPayments.Uid |  |
| RepPointLogUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPointLogs.Uid |  |
| Point | int | Hayir | ((0)) | Hayir |  |  |

## Crm.RepPaymentGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| GroupNo | nvarchar(100) | Evet |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| TransferDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.RepPayments

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir | Crm.Reps.Uid |  |
| RepGiftUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TotalPoint | int | Hayir |  | Hayir |  |  |
| TotalPaidAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| Status | nvarchar(50) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| InstallmentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RepPaymentGroupUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RepPaymentGroupNo | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.RepPointLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| RepPointUid | uniqueidentifier | Hayir |  | Hayir | Crm.RepPoints.Uid |  |
| Point | int | Hayir |  | Hayir |  |  |
| CustomerLoginUid | uniqueidentifier | Evet |  | Hayir | Crm.CustomerLogins.Uid |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| ActivityUid | uniqueidentifier | Evet |  | Hayir | Crm.Activities.Uid |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsPaid | bit | Hayir |  | Hayir |  |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsProvision | bit | Hayir | ((0)) | Hayir |  |  |
| PointPaid | int | Hayir | ((0)) | Hayir |  |  |
| InstallmentUid | uniqueidentifier | Evet |  | Hayir |  |  |
| AllowanceYear | int | Evet |  | Hayir |  |  |
| AllowanceMonth | int | Evet |  | Hayir |  |  |
| ContractPoint | int | Evet |  | Hayir |  |  |

## Crm.RepPoints

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Point | int | Hayir |  | Hayir |  |  |
| IsActive | bit | Hayir |  | Hayir |  |  |
| DayLimit | int | Evet |  | Hayir |  |  |
| Description | nvarchar(250) | Evet |  | Hayir |  |  |

## Crm.Reps

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Surname | nvarchar(100) | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| EMail | nvarchar(100) | Evet |  | Hayir |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| Iban | nvarchar(100) | Evet |  | Hayir |  |  |
| Tckno | nvarchar(50) | Evet |  | Hayir |  |  |
| Address | nvarchar(2000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| IsContract | bit | Evet |  | Hayir |  |  |
| ContractText | nvarchar(max) | Evet |  | Hayir |  |  |
| IsBlock | bit | Evet |  | Hayir |  |  |
| IsRecommend | bit | Evet |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir | Crm.Portfolios.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| ParentUid | uniqueidentifier | Evet |  | Hayir | Crm.Reps.Uid |  |
| CityUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| TownUid | uniqueidentifier | Evet |  | Hayir | Crm.Areas.Uid |  |
| OwnerRepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Image | nvarchar(50) | Evet |  | Hayir |  |  |
| HasPaymentCard | bit | Evet |  | Hayir |  |  |
| PushToken | nvarchar(200) | Evet |  | Hayir |  |  |
| PendingPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OldPortfolioUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OwnerUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Code | nvarchar(100) | Evet |  | Hayir |  |  |
| IsLogo | bit | Evet |  | Hayir |  |  |
| LogoID | nvarchar(100) | Evet |  | Hayir |  |  |
| DailyAdviceCount | int | Evet |  | Hayir |  |  |
| DailyAdviceDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsBrandEnvoy | bit | Evet |  | Hayir |  |  |
| LastAnnouncementUid | uniqueidentifier | Evet |  | Hayir |  |  |
| BankCode | nvarchar(100) | Evet |  | Hayir |  |  |
| IbanStatus | nvarchar(max) | Evet |  | Hayir |  |  |
| NotificationToken | nvarchar(max) | Evet |  | Hayir |  |  |
| NotificationId | nvarchar(max) | Evet |  | Hayir |  |  |
| BlockDate | datetime2(7) | Evet |  | Hayir |  |  |
| TotalPoint | int | Evet |  | Hayir |  |  |
| ProvisionPoint | int | Evet |  | Hayir |  |  |
| UsablePoint | int | Evet |  | Hayir |  |  |
| AdviceCount | int | Evet |  | Hayir |  |  |
| LeadCount | int | Evet |  | Hayir |  |  |
| CandidateCount | int | Evet |  | Hayir |  |  |
| CancelledCount | int | Evet |  | Hayir |  |  |
| ContractCount | int | Evet |  | Hayir |  |  |
| ContractCancelledCount | int | Evet |  | Hayir |  |  |
| AppointmentCount | int | Evet |  | Hayir |  |  |
| DontGoAppointmentCount | int | Evet |  | Hayir |  |  |
| PortfolioCode | varchar(10) | Evet |  | Hayir |  |  |
| PortfolioName | varchar(50) | Evet |  | Hayir |  |  |
| PortfolioOwner | uniqueidentifier | Evet |  | Hayir |  |  |
| PortfolioOrganization | uniqueidentifier | Evet |  | Hayir |  |  |
| OrganizationManagerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RegionManagerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UsedPoint | int | Evet |  | Hayir |  |  |
| RemainingPoint | int | Evet |  | Hayir |  |  |
| FutureDateNotPoint | int | Evet |  | Hayir |  |  |
| ExpiredDateNotPoint | int | Evet |  | Hayir |  |  |
| DontGoAppointmentRate | decimal(18,2) | Evet |  | Hayir |  |  |
| ContractCancelledRate | decimal(18,2) | Evet |  | Hayir |  |  |
| UnreachableAdvice | int | Evet |  | Hayir |  |  |
| CandidateRate | decimal(18,2) | Evet |  | Hayir |  |  |
| CancelledRate | decimal(18,2) | Evet |  | Hayir |  |  |
| UnreachableAdviceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| CallingRate | decimal(18,2) | Evet |  | Hayir |  |  |
| OrganizationName | varchar(100) | Evet |  | Hayir |  |  |
| RegionName | varchar(100) | Evet |  | Hayir |  |  |
| FirstAdviceDate | datetime2(7) | Evet |  | Hayir |  |  |
| LastAdviceDate | datetime2(7) | Evet |  | Hayir |  |  |
| BrandEnvoyDate | datetime2(7) | Evet |  | Hayir |  |  |
| TotalProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| TotalServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| ServiceRateAverage | decimal(18,2) | Evet |  | Hayir |  |  |
| PortfolioOwnerName | varchar(100) | Evet |  | Hayir |  |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SendUsedPointNotification | bit | Evet |  | Hayir |  |  |
| TaxNo | varchar(100) | Evet |  | Hayir |  |  |
| TaxOffice | varchar(100) | Evet |  | Hayir |  |  |
| SmsPassword | varchar(50) | Evet |  | Hayir |  |  |
| PasswordOld | varchar(50) | Evet |  | Hayir |  |  |
| LastPasswordChangeDate | datetime2(7) | Evet |  | Hayir |  |  |
| Salt | varchar(50) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| MeskenCustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| LastMoveMesken | bit | Evet |  | Hayir |  |  |
| DeviceId | varchar(200) | Evet |  | Hayir |  |  |
| IsRepInfoConfirm | bit | Evet |  | Hayir |  |  |
| RepInfoConfirmDate | datetime2(7) | Evet |  | Hayir |  |  |
| SmsSendDate | datetime2(7) | Evet |  | Hayir |  |  |
| ActivationToken | varchar(400) | Evet |  | Hayir |  |  |

## Crm.RestDays

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Date | datetime2(7) | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.RiskTrackingCosts

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| CostName | nvarchar(50) | Hayir |  | Hayir |  |  |
| CostPrice | decimal(18,2) | Hayir |  | Hayir |  |  |

## Crm.RiskTrackingLawyers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(400) | Hayir |  | Hayir |  |  |

## Crm.RiskTrackings

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| OrganizationName | nvarchar(50) | Hayir |  | Hayir |  |  |
| RegionUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| RegionName | nvarchar(50) | Hayir |  | Hayir |  |  |
| RiskTrackingLawyerUid | uniqueidentifier | Evet |  | Hayir | Crm.RiskTrackingLawyers.Uid |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Status | smallint | Hayir | ((0)) | Hayir |  |  |
| SubStatus | smallint | Hayir | ((0)) | Hayir |  |  |
| Year | smallint | Hayir |  | Hayir |  |  |
| TotalReceivableAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| NotificationStatus | smallint | Hayir | ((0)) | Hayir |  |  |
| FirstPostDate | datetime2(7) | Evet |  | Hayir |  |  |
| FirstNotificationDate | datetime2(7) | Evet |  | Hayir |  |  |
| FirstNoticeWageNo | nvarchar(50) | Evet |  | Hayir |  |  |
| FirstNoticeWageBarcodeNo | nvarchar(50) | Evet |  | Hayir |  |  |
| FirstPriceOfNotice | decimal(18,2) | Evet |  | Hayir |  |  |
| SecondPostDate | datetime2(7) | Evet |  | Hayir |  |  |
| SecondNotificationDate | datetime2(7) | Evet |  | Hayir |  |  |
| SecondPetitionWageNo | nvarchar(50) | Evet |  | Hayir |  |  |
| SecondPetitionWageBarcodeNo | nvarchar(50) | Evet |  | Hayir |  |  |
| SecondPriceOfNotice | decimal(18,2) | Evet |  | Hayir |  |  |
| ExecutionDate | datetime2(7) | Evet |  | Hayir |  |  |
| PaymentStatus | bit | Hayir | ((0)) | Hayir |  |  |
| ContractNo | nvarchar(50) | Evet |  | Hayir |  |  |
| ManagerApproveLimit | decimal(18,2) | Evet |  | Hayir |  |  |
| DelayStartInstallmentNumber | int | Evet |  | Hayir |  |  |
| DelayEndInstallmentNumber | int | Evet |  | Hayir |  |  |
| SynthTrackingAt | datetime2(7) | Evet |  | Hayir |  |  |
| EnforcementProceedingAt | datetime2(7) | Evet |  | Hayir |  |  |
| ClosedAt | datetime2(7) | Evet |  | Hayir |  |  |
| PaymentPromiseDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsSynth | bit | Evet | ((1)) | Hayir |  |  |

## Crm.Roles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Key | nvarchar(50) | Evet |  | Hayir |  |  |
| IsBranch | bit | Evet |  | Hayir |  |  |
| Description | nvarchar(100) | Evet |  | Hayir |  |  |
| HiddenReport | bit | Hayir | ((0)) | Hayir |  |  |
| IsResponsibleBranch | bit | Hayir | ((0)) | Hayir |  |  |

## Crm.RoleTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| ReferanceTarget | int | Hayir |  | Hayir |  |  |
| AppointmentTarget | int | Hayir |  | Hayir |  |  |
| ContractTarget | int | Hayir |  | Hayir |  |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| MaxReferanceScore | int | Evet |  | Hayir |  |  |
| MaxAppointmentScore | int | Evet |  | Hayir |  |  |
| MaxContractScore | int | Evet |  | Hayir |  |  |
| MaxGiroScore | int | Evet |  | Hayir |  |  |
| MaxReferanceScorePlus | int | Evet |  | Hayir |  |  |
| MaxAppointmentScorePlus | int | Evet |  | Hayir |  |  |
| MaxContractScorePlus | int | Evet |  | Hayir |  |  |
| MaxGiroScorePlus | int | Evet |  | Hayir |  |  |
| BranchCategoryUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PerformanceTarget | int | Evet |  | Hayir |  |  |
| MaxPerformanceScore | int | Evet |  | Hayir |  |  |
| MaxPerformanceScorePlus | int | Evet |  | Hayir |  |  |

## Crm.ScoreCards

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| TotalScore | decimal(18,2) | Hayir |  | Hayir |  |  |
| MarketingCount | int | Hayir |  | Hayir |  |  |
| ReferanceCount | int | Hayir |  | Hayir |  |  |
| ReferanceTarget | int | Hayir |  | Hayir |  |  |
| AppointmentCount | int | Hayir |  | Hayir |  |  |
| AppointmentTarget | int | Hayir |  | Hayir |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |
| ContractTarget | int | Hayir |  | Hayir |  |  |
| ContractPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  |  |
| CancellationAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| CancellationCount | int | Evet |  | Hayir |  |  |
| CancellationRate | decimal(18,2) | Evet |  | Hayir |  |  |
| SeveranceAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| SeveranceCount | decimal(18,2) | Evet |  | Hayir |  |  |
| SeveranceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| ParticipationFeeAverage | decimal(18,2) | Evet |  | Hayir |  |  |
| CashSaleRate | decimal(18,2) | Evet |  | Hayir |  |  |
| CashSaleCount | int | Evet |  | Hayir |  |  |
| CashGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| InstallmentGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| SpreadGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| PiecesGiroAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| CandidateCount | int | Evet |  | Hayir |  |  |
| HomeCandidateCount | int | Evet |  | Hayir |  |  |
| CarCandidateCount | int | Evet |  | Hayir |  |  |
| HomeCandidateRate | int | Evet |  | Hayir |  |  |
| FacebookCandidateCount | int | Evet |  | Hayir |  |  |
| InstagramCandidateCount | int | Evet |  | Hayir |  |  |
| GoogleCandidateCount | int | Evet |  | Hayir |  |  |
| OtherCandidateCount | int | Evet |  | Hayir |  |  |
| TabelaCount | int | Evet |  | Hayir |  |  |
| GoogleCandidateRate | int | Evet |  | Hayir |  |  |
| ExternalAppointmentCount | int | Evet |  | Hayir |  |  |
| Premium | decimal(18,2) | Evet |  | Hayir |  |  |
| PremiumMultiplier | decimal(18,2) | Evet |  | Hayir |  |  |
| TotalPremium | decimal(18,2) | Evet |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| PerformancePoint | int | Evet |  | Hayir |  |  |
| PerformanceTarget | int | Evet |  | Hayir |  |  |
| ContractPricePaid | decimal(18,2) | Evet |  | Hayir |  |  |
| ContractPriceUnPaid | decimal(18,2) | Evet |  | Hayir |  |  |
| MobileBrachCount | int | Evet |  | Hayir |  |  |

## Crm.ServiceConfigurationLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ServiceConfigurationUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Status | bit | Hayir |  | Hayir |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.ServiceConfigurations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Id | int | Hayir |  | Hayir |  |  |
| Name | varchar(200) | Evet |  | Hayir |  |  |
| Description | varchar(400) | Evet |  | Hayir |  |  |
| Link | varchar(200) | Evet |  | Hayir |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |
| FrequencyType | smallint | Hayir |  | Hayir |  |  |
| Frequency | int | Hayir |  | Hayir |  |  |
| StartDate | date | Hayir |  | Hayir |  |  |
| EndDate | date | Hayir |  | Hayir |  |  |
| WorkingStartDate | datetime | Evet |  | Hayir |  |  |
| WorkingEndDate | datetime | Evet |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| Parameters | varchar(400) | Evet |  | Hayir |  |  |
| SpecialTimeType | smallint | Evet |  | Hayir |  |  |
| SpecialStartDate | datetime | Evet |  | Hayir |  |  |
| SpecialEndDate | datetime | Evet |  | Hayir |  |  |
| SpecialTimeParameter | varchar(400) | Evet |  | Hayir |  |  |
| Priority | int | Hayir |  | Hayir |  |  |
| IsLogActive | bit | Hayir | ((0)) | Hayir |  |  |
| ListItemCount | int | Hayir |  | Hayir |  |  |

## Crm.ServiceLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ServiceUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Result | nvarchar(max) | Evet |  | Hayir |  |  |

## Crm.ServiceOthers

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Period | int | Hayir |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Link | nvarchar(200) | Evet |  | Hayir |  |  |
| Body | nvarchar(200) | Evet |  | Hayir |  |  |
| Priority | int | Evet |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| ProcessingStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| ProcessingEndDate | datetime2(7) | Evet |  | Hayir |  |  |
| ServiceId | smallint | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| StartHour | time(7) | Evet |  | Hayir |  |  |
| EndHour | time(7) | Evet |  | Hayir |  |  |

## Crm.ServiceRateRanges

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductUid | uniqueidentifier | Hayir |  | Hayir | Crm.Products.Uid |  |
| StartMonth | int | Hayir |  | Hayir |  |  |
| EndMonth | int | Hayir |  | Hayir |  |  |
| ServiceRateForBranch | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForRegion | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForGeneralManager | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateForCEO | decimal(18,2) | Hayir |  | Hayir |  |  |
| ServiceRateNotCampaign | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.Services

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedByUserUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Description | nvarchar(4000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Period | int | Hayir |  | Hayir |  |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| Link | nvarchar(200) | Evet |  | Hayir |  |  |
| Body | nvarchar(200) | Evet |  | Hayir |  |  |
| Priority | int | Evet |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| ProcessingStartDate | datetime2(7) | Evet |  | Hayir |  |  |
| ProcessingEndDate | datetime2(7) | Evet |  | Hayir |  |  |
| ServiceId | smallint | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| StartHour | time(7) | Evet |  | Hayir |  |  |
| EndHour | time(7) | Evet |  | Hayir |  |  |

## Crm.SetOffLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| RegionUid | uniqueidentifier | Evet |  | Hayir |  |  |
| PetitionDate | datetime2(7) | Evet |  | Hayir |  |  |
| TransactionDate | datetime2(7) | Evet |  | Hayir |  |  |
| PortfolioOwnerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| OldContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OldProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewProductUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OldContractCreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| NewContractCreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| OldIsDraw | bit | Hayir |  | Hayir |  |  |
| NewIsDraw | bit | Hayir |  | Hayir |  |  |
| OldServiceType | nvarchar(5) | Evet |  | Hayir |  |  |
| NewServiceType | nvarchar(5) | Evet |  | Hayir |  |  |
| OldProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| NewProductPrice | decimal(18,2) | Evet |  | Hayir |  |  |
| OldServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| NewServicePrice | decimal(18,2) | Evet |  | Hayir |  |  |
| Status | nvarchar(5) | Evet |  | Hayir |  |  |
| SubStatus | nvarchar(5) | Evet |  | Hayir |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |
| Year | int | Evet |  | Hayir |  |  |
| Month | int | Evet |  | Hayir |  |  |
| ProductPriceDifference | decimal(18,2) | Evet |  | Hayir |  |  |
| ServicePriceDifference | decimal(18,2) | Evet |  | Hayir |  |  |
| NewContractStatus | nvarchar(3) | Evet |  | Hayir |  |  |
| OldContractTotalPaid | decimal(18,2) | Evet |  | Hayir |  |  |
| BidApprovalRole | varchar(5) | Evet |  | Hayir |  |  |
| FileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OldContractServiceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| NewContractServiceRate | decimal(18,2) | Evet |  | Hayir |  |  |
| OldContractSalesPerson | uniqueidentifier | Evet |  | Hayir |  |  |
| NewContractSalesPerson | uniqueidentifier | Evet |  | Hayir |  |  |
| PostVirmanQueueUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OldContractSalesOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |
| NewContractSalesOrganizationUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.SetOffProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| SetOffLogUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| Department | uniqueidentifier | Evet |  | Hayir |  |  |
| Description | nvarchar(500) | Evet |  | Hayir |  |  |
| SetOffProcessType | smallint | Hayir |  | Hayir |  |  |

## Crm.Simulations

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| OwnerUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| ProductPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| InstallmentPrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| CachePrice | decimal(18,2) | Hayir |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| SimulationUid | uniqueidentifier | Evet |  | Hayir | Crm.Simulations.Uid |  |
| IsMesken | bit | Evet |  | Hayir |  |  |

## Crm.SmsGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| SmsTemplateUid | uniqueidentifier | Evet |  | Hayir | Crm.SmsTemplates.Uid |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| CompletedDate | datetime2(7) | Evet |  | Hayir |  |  |
| SearchQuery | nvarchar(100) | Evet |  | Hayir |  |  |
| IsCompleted | bit | Hayir |  | Hayir |  |  |

## Crm.SmsLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  |  |
| SmsGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.SmsGroups.Uid |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir | Crm.Customers.Uid |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir | Crm.Contracts.Uid |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid |  |
| IsSent | bit | Hayir |  | Hayir |  |  |
| OpportunityUid | uniqueidentifier | Evet |  | Hayir | Crm.Opportunities.Uid |  |

## Crm.SmsTemplates

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Text | nvarchar(4000) | Evet |  | Hayir |  |  |
| Type | nvarchar(50) | Evet |  | Hayir |  |  |
| Key | nvarchar(100) | Evet |  | Hayir |  |  |
| IsNotification | bit | Evet |  | Hayir |  |  |
| Title | nvarchar(100) | Evet |  | Hayir |  |  |
| Enabled | bit | Evet | ((0)) | Hayir |  |  |
| IsSms | bit | Evet | ((0)) | Hayir |  |  |
| TestPhoneNumber | nvarchar(10) | Evet |  | Hayir |  |  |
| PhoneJSonList | nvarchar(500) | Evet |  | Hayir |  |  |

## Crm.SmsVerificationCodes

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| LeadUid | uniqueidentifier | Evet |  | Hayir | Crm.Leads.Uid |  |
| VerificationCode | nvarchar(50) | Hayir |  | Hayir |  |  |
| Type | smallint | Hayir |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Hayir |  | Hayir |  |  |
| ExpirationDateTime | datetime | Hayir |  | Hayir |  |  |
| IsUsed | bit | Hayir | ((0)) | Hayir |  |  |

## Crm.SustainabilityFeatureValues

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| FeatureType | smallint | Hayir |  | Hayir |  |  |
| Key | nvarchar(50) | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Hayir |  | Hayir |  |  |
| Order | int | Hayir |  | Hayir |  |  |

## Crm.SustainabilityReports

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ProductType | nvarchar(50) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Hayir |  | Hayir | Crm.Contracts.Uid |  |
| MortgagesUid | uniqueidentifier | Hayir |  | Hayir | Crm.Mortgages.Uid |  |
| MortgagePledgeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgagePledges.Uid |  |
| FeatureType | smallint | Hayir |  | Hayir |  |  |
| FeatureValueUid | uniqueidentifier | Evet |  | Hayir | Crm.SustainabilityFeatureValues.Uid |  |
| MortgageTypeUid | uniqueidentifier | Evet |  | Hayir | Crm.MortgageTypes.Uid |  |
| VehicleRegistrationType | smallint | Evet |  | Hayir |  |  |

## Crm.TakbisCity

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |

## Crm.TakbisHomeTown

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| Status | nvarchar(250) | Evet |  | Hayir |  |  |
| Type | nvarchar(250) | Evet |  | Hayir |  |  |
| TownId | int | Evet |  | Hayir |  |  |
| IsActive | bit | Evet |  | Hayir |  |  |

## Crm.TakbisInsuranceCompanies

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |
| Name | nvarchar(250) | Evet |  | Hayir |  |  |

## Crm.TakbisTown

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| TakbisId | int | Evet |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| CityId | int | Evet |  | Hayir |  |  |

## Crm.TicketHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| TicketUid | uniqueidentifier | Hayir |  | Hayir | Crm.Tickets.Uid |  |
| UpdatedName | nvarchar(200) | Evet |  | Hayir |  |  |
| FieldName | nvarchar(100) | Evet |  | Hayir |  |  |
| OldValue | nvarchar(50) | Evet |  | Hayir |  |  |
| NewValue | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.Tickets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Title | nvarchar(max) | Evet |  | Hayir |  |  |
| Description | nvarchar(max) | Evet |  | Hayir |  |  |
| OwnerUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DepartmentUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| RequestingPersonUid | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Priority | nvarchar(max) | Evet |  | Hayir |  |  |
| Type | nvarchar(max) | Evet |  | Hayir |  |  |
| Status | nvarchar(max) | Evet |  | Hayir |  |  |
| DeadLine | datetime2(7) | Evet |  | Hayir |  |  |
| CompletedBy | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.tmpAllGroupInfo

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| Name | nvarchar(20) | Hayir |  | Hayir |  |  |
| InstallmentCount | int | Hayir |  | Hayir |  |  |
| GroupDate | datetime | Hayir |  | Hayir |  |  |
| IsOpen | bit | Hayir |  | Hayir |  |  |
| Type | nvarchar(3) | Evet |  | Hayir |  |  |
| JokerCount | int | Hayir |  | Hayir |  |  |
| ContractCount | int | Hayir |  | Hayir |  |  |
| TotalSelectCount | int | Hayir |  | Hayir |  |  |
| ContractSelectCount | int | Hayir |  | Hayir |  |  |
| JokerSelectCount | int | Hayir |  | Hayir |  |  |
| MaxDeliveryDate | datetime | Evet |  | Hayir |  |  |
| SelectCount | int | Hayir |  | Hayir |  |  |
| LastOrganizationDate | datetime | Evet |  | Hayir |  |  |
| CreatedAt | datetime | Evet |  | Hayir |  |  |
| MaxDeliveryLastInstallment | int | Hayir |  | Hayir |  |  |
| CreatedBy | nvarchar(100) | Evet |  | Hayir |  |  |
| ClosedBy | nvarchar(100) | Evet |  | Hayir |  |  |
| StartDate | datetime | Evet |  | Hayir |  |  |
| EndDate | datetime | Evet |  | Hayir |  |  |
| Status | nvarchar(3) | Evet |  | Hayir |  |  |
| IsMesken | bit | Evet |  | Hayir |  |  |
| NextDraw | nvarchar(4) | Evet |  | Hayir |  |  |
| MaxDeliveryMonth | int | Hayir |  | Hayir |  |  |
| FirstOrganizationDate | datetime | Evet |  | Hayir |  |  |
| LastDrawDate | datetime | Evet |  | Hayir |  |  |
| NextDrawDate | datetime | Evet |  | Hayir |  |  |
| NextDrawPeriod | nvarchar(4) | Evet |  | Hayir |  |  |
| BallCount | int | Hayir |  | Hayir |  |  |
| TotalDrawBall | int | Hayir |  | Hayir |  |  |

## Crm.UnauthorizedProcessLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Evet |  | Hayir | Crm.Organizations.Uid |  |
| ModuleKey | nvarchar(400) | Evet |  | Hayir |  |  |
| Key | nvarchar(400) | Evet |  | Hayir |  |  |

## Crm.UserHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| StartDate | datetime2(7) | Hayir |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| PortfolioUid | uniqueidentifier | Evet |  | Hayir | Crm.Portfolios.Uid |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.UserLeaveDetails

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Evet | ((0)) | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| EndDate | datetime2(7) | Evet |  | Hayir |  |  |
| StartHour | datetime2(7) | Evet |  | Hayir |  |  |
| EndHour | datetime2(7) | Evet |  | Hayir |  |  |
| AnnualLeaveModel | bit | Evet |  | Hayir |  |  |
| AnnualLeaveType | int | Evet |  | Hayir |  |  |
| Description | varchar(300) | Evet |  | Hayir |  |  |
| CancelDescription | varchar(300) | Evet |  | Hayir |  |  |
| Status | smallint | Evet |  | Hayir |  |  |
| CancelDate | datetime2(7) | Evet |  | Hayir |  |  |
| CancelBy | uniqueidentifier | Evet |  | Hayir |  |  |
| ApprovalDate | datetime2(7) | Evet |  | Hayir |  |  |
| ApprovalBy | uniqueidentifier | Evet |  | Hayir |  |  |
| ProxyUserUid | uniqueidentifier | Evet |  | Hayir |  |  |
| InternalFileUid | uniqueidentifier | Evet |  | Hayir |  |  |
| IsUser | bit | Evet |  | Hayir |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |
| SubStatus | smallint | Evet |  | Hayir |  |  |

## Crm.UserLeavePermission

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Hayir |  |  |
| AnnualLeaveModel | int | Evet |  | Hayir |  |  |
| AnnualLeaveType | int | Evet |  | Hayir |  |  |
| PermissionName | varchar(max) | Evet |  | Hayir |  |  |
| ProgressDay | int | Evet |  | Hayir |  |  |

## Crm.UserLeaves

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Evet | ((0)) | Hayir |  |  |
| Seniority | int | Evet |  | Hayir |  |  |
| DeservedLeave | int | Evet |  | Hayir |  |  |
| TotalDeservedLeave | int | Evet |  | Hayir |  |  |
| DelegatedPermission | decimal(18,2) | Evet |  | Hayir |  |  |
| PermissionUsed | decimal(18,2) | Evet |  | Hayir |  |  |
| RemainingLeave | decimal(18,2) | Evet |  | Hayir |  |  |
| IsUser | bit | Evet |  | Hayir |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |

## Crm.UserLogins

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| IP | nvarchar(100) | Evet |  | Hayir |  |  |
| Host | nvarchar(100) | Evet |  | Hayir |  |  |
| Browser | nvarchar(100) | Evet |  | Hayir |  |  |
| Authority | nvarchar(max) | Evet |  | Hayir |  |  |
| LastConnectDate | datetime2(7) | Hayir |  | Hayir |  |  |
| IsCrm | bit | Evet |  | Hayir |  |  |
| IsLdap | bit | Evet |  | Hayir |  |  |

## Crm.UserPasswordHistories

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir |  |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| RepUid | uniqueidentifier | Evet |  | Hayir |  |  |
| CustomerUid | uniqueidentifier | Evet |  | Hayir |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| Salt | varchar(100) | Evet |  | Hayir |  |  |
| ExpireDate | datetime2(7) | Evet |  | Hayir |  |  |
| HashType | smallint | Evet |  | Hayir |  |  |
| Platform | smallint | Evet |  | Hayir |  |  |

## Crm.UserPortfolios

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid1 | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir |  |  |
| PortfolioUid | uniqueidentifier | Hayir |  | Hayir | Crm.Portfolios.Uid |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.UserResponsibleBranches

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir | ((0)) | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| BranchUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |

## Crm.UserRoles

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| RoleUid | uniqueidentifier | Hayir |  | Hayir | Crm.Roles.Uid |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |

## Crm.Users

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| EMail | nvarchar(50) | Evet |  | Hayir |  |  |
| HomePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| MobilePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| Gender | nvarchar(10) | Evet |  | Hayir |  |  |
| UserName | nvarchar(100) | Evet |  | Hayir |  |  |
| Password | nvarchar(100) | Evet |  | Hayir |  |  |
| NewPassword | nvarchar(100) | Evet |  | Hayir |  |  |
| IsUser | bit | Hayir |  | Hayir |  |  |
| StartDate | datetime2(7) | Evet |  | Hayir |  |  |
| LeaveDate | datetime2(7) | Evet |  | Hayir |  |  |
| OrganizationUid | uniqueidentifier | Hayir |  | Hayir | Crm.Organizations.Uid |  |
| LastCustomerAssignDate | datetime2(7) | Evet |  | Hayir |  |  |
| LastBranchCustomerAssignDate | datetime2(7) | Evet |  | Hayir |  |  |
| IsBusy | bit | Hayir | ((0)) | Hayir |  |  |
| EMail2 | nvarchar(50) | Evet |  | Hayir |  |  |
| Code | nvarchar(100) | Evet |  | Hayir |  |  |
| IsManager | bit | Hayir | ((0)) | Hayir |  |  |
| LastAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  |  |
| InternalPhone | nvarchar(50) | Evet |  | Hayir |  |  |
| Image | nvarchar(200) | Evet |  | Hayir |  |  |
| Tckno | nvarchar(50) | Evet |  | Hayir |  |  |
| IBAN | nvarchar(50) | Evet |  | Hayir |  |  |
| CostCode | nvarchar(100) | Evet |  | Hayir |  |  |
| CurrentCode | nvarchar(100) | Evet |  | Hayir |  |  |
| DateOfBirth | datetime2(7) | Evet |  | Hayir |  |  |
| LastDeskAppointmentAssignDate | datetime2(7) | Evet |  | Hayir |  |  |
| RepCode | nvarchar(100) | Evet |  | Hayir |  |  |
| PartnerName | nvarchar(100) | Evet |  | Hayir |  |  |
| PartnerTc | nvarchar(50) | Evet |  | Hayir |  |  |
| PartnerPhone | nvarchar(50) | Evet |  | Hayir |  |  |
| MeskenUid | uniqueidentifier | Evet |  | Hayir |  |  |
| SamAccountName | nvarchar(50) | Evet |  | Hayir |  |  |
| ResetLdapPassword | bit | Evet |  | Hayir |  |  |
| ResetPassword | bit | Evet |  | Hayir |  |  |
| FirstName | nvarchar(100) | Evet |  | Hayir |  |  |
| Surname | nvarchar(100) | Evet |  | Hayir |  |  |
| LoginFailedCount | smallint | Hayir | ((0)) | Hayir |  |  |
| SecondCurrentCode | nvarchar(100) | Evet |  | Hayir |  |  |
| UType | int | Hayir | ((1)) | Hayir |  |  |
| PathStatus | smallint | Hayir | ((1)) | Hayir |  |  |
| TransferDescription | nvarchar(500) | Evet |  | Hayir |  |  |
| IsVisibleMobilePhone | bit | Hayir | ((1)) | Hayir |  |  |
| PrivatePhone | nvarchar(50) | Evet |  | Hayir |  |  |
| LeaveType | smallint | Evet |  | Hayir |  |  |
| LeaveSubType | int | Evet |  | Hayir |  |  |
| IsNewHash | bit | Evet |  | Hayir |  |  |
| OutSourceEmail | nvarchar(50) | Evet |  | Hayir |  |  |

## Crm.UserTargets

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| UserUid | uniqueidentifier | Hayir |  | Hayir | Crm.Users.Uid |  |
| ReferanceTarget | int | Hayir |  | Hayir |  |  |
| AppointmentTarget | int | Hayir |  | Hayir |  |  |
| ContractTarget | int | Hayir |  | Hayir |  |  |
| Month | int | Hayir |  | Hayir |  |  |
| Year | int | Hayir |  | Hayir |  |  |
| GiroTarget | decimal(18,2) | Hayir |  | Hayir |  |  |
| MaxReferanceScore | int | Hayir |  | Hayir |  |  |
| MaxAppointmentScore | int | Hayir |  | Hayir |  |  |
| MaxContractScore | int | Hayir |  | Hayir |  |  |
| MaxGiroScore | int | Hayir |  | Hayir |  |  |
| MaxReferanceScorePlus | int | Hayir |  | Hayir |  |  |
| MaxAppointmentScorePlus | int | Hayir |  | Hayir |  |  |
| MaxContractScorePlus | int | Hayir |  | Hayir |  |  |
| MaxGiroScorePlus | int | Hayir |  | Hayir |  |  |
| PerformanceTarget | int | Evet |  | Hayir |  |  |
| MaxPerformanceScore | int | Evet |  | Hayir |  |  |
| MaxPerformanceScorePlus | int | Evet |  | Hayir |  |  |

## Crm.VariableIndexGroups

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Name | nvarchar(100) | Evet |  | Hayir |  |  |
| ShortName | nvarchar(100) | Evet |  | Hayir |  |  |
| IsRate | bit | Hayir |  | Hayir |  |  |

## Crm.VariableIndexs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| Rate | decimal(18,2) | Hayir |  | Hayir |  |  |
| Value | decimal(18,2) | Hayir |  | Hayir |  |  |
| Date | datetime2(7) | Hayir |  | Hayir |  |  |
| VariableIndexGroupUid | uniqueidentifier | Evet |  | Hayir | Crm.VariableIndexGroups.Uid |  |

## Crm.VirtualPosCommisions

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| BanklogUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| TotalAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| CommisionAmount | decimal(18,2) | Hayir |  | Hayir |  |  |
| CommisionRate | decimal(18,2) | Hayir |  | Hayir |  |  |
| CashCommisionRate | decimal(18,2) | Evet |  | Hayir |  |  |
| CashCommisionAmount | decimal(18,2) | Evet |  | Hayir |  |  |

## Crm.VirtualPosLogs

| Kolon | Veri Tipi | Null | Varsayilan | PK | FK Referans | Not |
|---|---|---|---|---|---|---|
| Uid | uniqueidentifier | Hayir |  | Evet |  |  |
| UpdatedAt | datetime2(7) | Evet |  | Hayir |  |  |
| DeletedAt | datetime2(7) | Evet |  | Hayir |  |  |
| CreatedAt | datetime2(7) | Hayir |  | Hayir |  |  |
| CreatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| UpdatedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| DeletedBy | uniqueidentifier | Evet |  | Hayir | Crm.Users.Uid |  |
| Deleted | bit | Hayir |  | Hayir |  |  |
| ContractUid | uniqueidentifier | Evet |  | Hayir |  |  |
| OrderId | nvarchar(100) | Evet |  | Hayir |  |  |
| MerchantID | nvarchar(100) | Evet |  | Hayir |  |  |
| Amount | decimal(18,2) | Hayir |  | Hayir |  |  |
| MD | nvarchar(500) | Evet |  | Hayir |  |  |
| HashData | nvarchar(200) | Evet |  | Hayir |  |  |
| Response | nvarchar(100) | Evet |  | Hayir |  |  |
| ProvisionNumber | nvarchar(200) | Evet |  | Hayir |  |  |
| RRN | nvarchar(200) | Evet |  | Hayir |  |  |
| Stan | nvarchar(200) | Evet |  | Hayir |  |  |
| ResponseMessage | nvarchar(200) | Evet |  | Hayir |  |  |
| ResponseCode | nvarchar(200) | Evet |  | Hayir |  |  |
| MerchantOrderId | nvarchar(200) | Evet |  | Hayir |  |  |
| BankCode | nvarchar(200) | Evet |  | Hayir |  |  |
| Status | smallint | Hayir |  | Hayir |  |  |
| Message | nvarchar(max) | Evet |  | Hayir |  |  |
| BankLogUid | uniqueidentifier | Evet |  | Hayir |  |  |
| InQueue | bit | Hayir | ((0)) | Hayir |  |  |
| CommisionAmount | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| CommisionRate | decimal(18,2) | Hayir | ((0)) | Hayir |  |  |
| InstallmentCount | int | Evet | ((1)) | Hayir |  |  |
| PaymentDate | datetime2(7) | Evet |  | Hayir |  |  |
| CashCommisionRate | decimal(18,2) | Evet |  | Hayir |  |  |
| CashCommisionAmount | decimal(18,2) | Evet |  | Hayir |  |  |
| CanPayServicePriceInstbyVP | bit | Evet |  | Hayir |  |  |
| LogoStatus | smallint | Evet |  | Hayir |  |  |
| PosId | int | Evet |  | Hayir |  |  |

