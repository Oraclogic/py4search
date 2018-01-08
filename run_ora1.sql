spool sp1.txt
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss'),host_name,instance_name date_time from v$instance;
begin
  dbms_lock.sleep(10);
end;
/
spool off
