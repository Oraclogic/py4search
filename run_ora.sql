spool sp.txt
SET linesize 200 col log_date
FOR a25 col instance_name
FOR a16 col host_name
FOR a30
SELECT to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') log_date,
       host_name,
       instance_name,
       username||chr(10)
FROM v$instance,
      dba_users;

 spool OFF
