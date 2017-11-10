spool C:\Users\IBM_ADMIN\PycharmProjects\sp.txt
set linesize 200
col log_date for a25
col instance_name  for a16
col host_name for a30
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') log_date,host_name,instance_name from v$instance;
spool off