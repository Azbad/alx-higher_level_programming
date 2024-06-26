-- Lists all cities in the database hbtn_0d_usa.
-- Results are sorted by cities.id in ascending order.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
