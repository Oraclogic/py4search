spool sp2.txt
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss'),host_name,instance_name date_time from v$instance;
spool off