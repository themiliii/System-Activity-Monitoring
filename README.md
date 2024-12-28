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


Usage | نحوه استفاده
Download the project files and save them to your system.

The program will automatically begin monitoring system activities and display event logs, file changes, network activity, and hardware status in the console.

You can view the output directly in the terminal and track any unusual or suspicious activity.

فایل‌های پروژه را دانلود کرده و در سیستم خود ذخیره کنید.

برنامه به طور خودکار شروع به نظارت بر فعالیت‌های سیستم کرده و لاگ‌های رویداد، تغییرات فایل، فعالیت‌های شبکه و وضعیت سخت‌افزار را در کنسول نمایش می‌دهد.

شما می‌توانید خروجی را مستقیماً در ترمینال مشاهده کرده و هرگونه فعالیت غیرعادی یا مشکوک را ردیابی کنید.

How to Run | نحوه اجرای برنامه
To run the program, open a command prompt and enter the following:

برای اجرای برنامه، یک پنجره دستور (Command Prompt) باز کرده و دستور زیر را وارد کنید:

bash
Copy code
python path_to_the_script.py
Example | مثال:
bash
Copy code
python C:\Users\iTakPC\Desktop\show-security-protocols.py
This will start the monitoring process and display system events in the terminal.

این دستور فرایند نظارت را آغاز کرده و رویدادهای سیستم را در ترمینال نمایش می‌دهد.

Code Overview | بررسی کد
Event Logs Monitoring | نظارت بر لاگ‌های رویداد
The program uses win32evtlog to access and read Windows Event Logs. It retrieves different system events, such as errors, warnings, and informational logs that the system records.

این برنامه از win32evtlog برای دسترسی و خواندن لاگ‌های رویداد ویندوز استفاده می‌کند. این برنامه رویدادهای مختلف سیستم مانند خطاها، هشدارها و لاگ‌های اطلاع‌رسانی که سیستم ثبت می‌کند را بازیابی می‌کند.

Network Activity Monitoring | نظارت بر فعالیت‌های شبکه
Using psutil and wmi, the program monitors network connections, USB devices, and system processes.

با استفاده از psutil و wmi، این برنامه به نظارت بر اتصالات شبکه، دستگاه‌های USB و فرآیندهای سیستم می‌پردازد.

File Monitoring | نظارت بر فایل‌ها
The watchdog library is used to monitor file system changes, such as additions, deletions, and modifications to files and folders.

کتابخانه watchdog برای نظارت بر تغییرات سیستم فایل، مانند اضافه شدن، حذف و تغییرات فایل‌ها و پوشه‌ها استفاده می‌شود.

Reports and Output | گزارش‌ها و خروجی‌ها
The output of the program is displayed in the console, and you can modify the program to log these events into a file for further analysis.

خروجی برنامه در کنسول نمایش داده می‌شود و شما می‌توانید برنامه را طوری تنظیم کنید که این رویدادها را در فایلی برای تحلیل‌های بیشتر ذخیره کند.

Security Considerations | ملاحظات امنیتی
Accessing Event Logs requires administrative privileges. Therefore, you must run the program in an administrator environment.

Monitoring hardware devices, such as USBs, also requires elevated privileges to access hardware status.

دسترسی به لاگ‌های رویداد نیازمند دسترسی‌های مدیریتی است. بنابراین، باید برنامه را در محیط مدیر سیستم (Administrator) اجرا کنید.

نظارت بر دستگاه‌های سخت‌افزاری مانند USB‌ها نیز نیازمند دسترسی‌های بالا برای دسترسی به وضعیت سخت‌افزار است.

Contributing | مشارکت
If you would like to contribute to this project or add new features, please create an Issue or submit a Pull Request.

اگر تمایل به مشارکت در این پروژه یا اضافه کردن ویژگی‌های جدید دارید، لطفاً یک Issue بسازید یا Pull Request ارسال کنید.

License | مجوز
This project is licensed under the MIT License. You can freely use, modify, and distribute it.

این پروژه تحت مجوز MIT License منتشر شده است. شما می‌توانید به‌راحتی از آن استفاده کرده، تغییرات دهید و توزیع کنید.
