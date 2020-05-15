### Скрипт для ручной очистки файлов и папок, записывает в .log-файл дату удаления и имя файла/папки

Write-Host "Удаление неиспользуемых файлов старше 30 дней и очистка от пустых папок"
Read-Host "Для продолжения нажмите Enter"
#Задаём дату удаления
$DelDays = (Get-Date).AddDays(-30)
#Папка назначения
$targetpath = "C:\Personal"

$timestamp = Get-Date | ForEach-Object { $_ -replace ":", "." }
$filename = $targetpath+$timestamp + '.log'

#Удаляем файлы в папке назначения согласно дате удаления
$files = Get-ChildItem -Path $targetpath -Recurse -Force | Where-Object { !$_.PSIsContainer  -and $_.LastWriteTime -lt $DelDays } #| Remove-Item -Force -Verbose 4>&1 | Set-Content $filename
Set-Content $filename -value 'LOG'
foreach ($i in $files){
    $timestamp = Get-Date | ForEach-Object { $_ -replace ":", "." }
    Add-Content $filename -Value $timestamp, $i
    Remove-Item $i.FullName -Force 
}
#Удаляем все пустые папки в назначенной директории
Get-ChildItem -Path $targetpath -Recurse -Force | Where-Object { $_.PSIsContainer -and (Get-ChildItem -Path $_.FullName -Recurse -Force | Where-Object { !$_.PSIsContainer }) -eq $null } | Remove-Item -Force -Recurse -Verbose 4>&1 | Add-Content 'D:\Logs\Clear.log'
#Сообщаем о заверешении и предлагаем выйти из среды обработки
Write-Host "`nУдаление и очистка завершены"
#Read-Host "Для выхода нажмите Enter"
