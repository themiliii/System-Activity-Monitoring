# System Activity Monitoring | نظارت بر فعالیت‌های سیستم

This project is designed to monitor various system activities on Windows. It collects and analyzes system event logs, hardware status, and file changes, focusing on security-related events and system behavior tracking. The goal of this program is to monitor and log system activities to help identify issues and track changes.

این پروژه برای نظارت بر فعالیت‌های مختلف سیستم در ویندوز طراحی شده است. این برنامه به جمع‌آوری و تجزیه و تحلیل لاگ‌های رویداد سیستم، وضعیت سخت‌افزار و تغییرات فایل‌ها پرداخته و بر رویدادهای امنیتی و رفتار سیستم تمرکز دارد. هدف از این برنامه نظارت و ثبت فعالیت‌های سیستم برای شناسایی مشکلات و ردیابی تغییرات است.

## Features | ویژگی‌ها

- **System Event Logs Monitoring**: The program collects and displays event logs from Windows Event Viewer. It shows Event IDs, time stamps, source names, and messages associated with system events.
  
- **Hardware Activity Monitoring**: It can track hardware-related activities, such as **USB device connections/disconnections** and other hardware-related events.

- **File and Folder Activity Monitoring**: The program uses the `watchdog` library to continuously monitor file and folder changes. It logs any modifications, deletions, or additions.

- **Network Activity Monitoring**: It monitors network connections and can detect suspicious or unauthorized network activities.

- **Reporting and Logging**: All system activities are logged, and reports are generated, which can be used for further analysis.

- **نظارت بر لاگ‌های رویداد سیستم**: برنامه لاگ‌های رویداد ویندوز را جمع‌آوری و نمایش می‌دهد. این لاگ‌ها شامل شناسه‌های رویداد، زمان، نام منابع و پیام‌های مرتبط با رویدادهای سیستم است.

- **نظارت بر فعالیت‌های سخت‌افزاری**: این برنامه می‌تواند فعالیت‌های مربوط به سخت‌افزار، مانند اتصال/قطع اتصال دستگاه‌های USB و دیگر رویدادهای سخت‌افزاری را ردیابی کند.

- **نظارت بر فعالیت‌های فایل و پوشه**: برنامه از کتابخانه `watchdog` برای نظارت مستمر بر تغییرات فایل‌ها و پوشه‌ها استفاده می‌کند. هرگونه تغییر، حذف یا اضافه شدن فایل‌ها را ثبت می‌کند.

- **نظارت بر فعالیت‌های شبکه**: این برنامه فعالیت‌های شبکه را نظارت کرده و قادر است فعالیت‌های مشکوک یا غیرمجاز را شناسایی کند.

- **گزارش‌دهی و ثبت اطلاعات**: تمام فعالیت‌های سیستم ثبت شده و گزارش‌هایی برای تحلیل‌های بیشتر تولید می‌شود.

## Prerequisites | پیش‌نیازها

To run this program, you need to install the following Python libraries:

- **pywin32**: For interacting with Windows APIs and reading Event Logs.
- **watchdog**: For monitoring file and folder changes.
- **wmi**: For hardware status and device monitoring.
- **psutil**: For process and system resource monitoring.

To install these dependencies, you can use the following command:

برای اجرای این برنامه، باید کتابخانه‌های پایتون زیر را نصب کنید:

- **pywin32**: برای تعامل با APIهای ویندوز و خواندن لاگ‌های رویداد.
- **watchdog**: برای نظارت بر تغییرات فایل‌ها و پوشه‌ها.
- **wmi**: برای نظارت بر وضعیت سخت‌افزار و دستگاه‌ها.
- **psutil**: برای نظارت بر فرآیندها و منابع سیستم.

برای نصب این وابستگی‌ها، می‌توانید از دستور زیر استفاده کنید:

```bash
pip install pywin32 watchdog wmi psutil
