-- 1
create or replace trigger log_takes
after update on takes
for each row
BEGIN
  insert into log_change_takes values (SYSDATE, :NEW.id, :NEW.course_id, :NEW.sec_id, :NEW.semester, :NEW.year, :NEW.grade);
END;
/

-- 2
create or replace trigger log_salary
after update on instructor
for each row
WHEN (OLD.salary <> NEW.salary)
BEGIN
  insert into old_date_instructor values(:OLD.id, :OLD.name, :OLD.dept_name, :OLD.salary);
END;
/

-- 3
create or replace trigger
before insert on instructor
DECLARE
  v_budget department.budget%type;
BEGIN
  if not regexp_like(:NEW.name, '^[a-zA-Z]+$') then
    raise_application_error(-20001, 'Instructor name must have only alphabets');
  end if;
  if (:NEW.salary < 1) then
    raise_application_error(-20002, 'Instructor salary must be positive');
  end if;
  select budget into v_budget from department where dept_name = :NEW.dept_name;
  if(:NEW.salary > v_budget) then
    raise_application_error(-20003, 'Salary cannot exceed budget');
  end if;
END;
/

-- 4
create or replace trigger auditor
before delete or update on client_master
for each row
DECLARE
  op varchar2(10);
BEGIN
  case
    when deleting then op := 'delete';
    when updating then op := 'update';
  end case;
  insert into auditclient values (:OLD.client_no, :OLD.name, :OLD.bal_due, op, USER, SYSDATE);
END;
/
