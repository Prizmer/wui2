SELECT 
  objects.name,
  right('00'::text||substring(objects.name from 10), 3)
FROM 
  public.objects
WHERE 
  objects.name LIKE '%Квартира%';
