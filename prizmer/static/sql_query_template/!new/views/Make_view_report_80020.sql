CREATE OR REPLACE VIEW report_80020 AS 
SELECT 
                          groups_80020.name_sender, 
                          groups_80020.inn_sender, 
                          groups_80020.dogovor_number, 
                          meters.factory_number_manual, 
                          link_groups_80020_meters.measuringpoint_name, 
                          link_groups_80020_meters.measuringpoint_code, 
                          meters.dt_last_read,
                          groups_80020.name as group_name
                        FROM 
                          public.meters, 
                          public.groups_80020, 
                          public.link_groups_80020_meters
                        WHERE 
                          link_groups_80020_meters.guid_meters = meters.guid AND
                          link_groups_80020_meters.guid_groups_80020 = groups_80020.guid AND
                          groups_80020.name = '80020'