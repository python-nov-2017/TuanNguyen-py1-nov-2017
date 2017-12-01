-- 1. What query would you run to get the total revenue for March of 2012?
SELECT monthname(charged_datetime) as month, sum(amount) as revenue
FROM billing
WHERE month(charged_datetime)=3 AND year(charged_datetime) = '2012';

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, sum(amount) as total_revenue
FROM billing
WHERE client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT domain_name as website, client_id
FROM sites
WHERE client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT client_id, count(domain_name), monthname(created_datetime) as month_created, year(created_datetime) as year_created
FROM sites
WHERE client_id = 1
GROUP BY month_created, year_created;

SELECT client_id, count(domain_name), monthname(created_datetime) as month_created, year(created_datetime) as year_created
FROM sites
WHERE client_id = 20
GROUP BY month_created, year_created;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT domain_name as website, count(leads.leads_id) as number_of_leads, date_format(registered_datetime, '%M %d, %Y') as date_generated
FROM sites
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN '2011/01/01' AND '2011/02/15'
GROUP BY website;

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, count(leads.leads_id) as number_of_leads
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/12/31'
GROUP BY client_name;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, count(leads.leads_id) as number_of_leads, monthname(leads.registered_datetime) as month_generated
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/06/30'
GROUP BY leads.leads_id
ORDER BY month(leads.registered_datetime), clients.client_id;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, sites.domain_name as websites, count(leads.leads_id) as number_of_leads, monthname(leads.registered_datetime) as month_generated
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/12/31'
GROUP BY sites.site_id
ORDER BY clients.client_id;

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, sites.domain_name as websites, count(leads.leads_id) as number_of_leads
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
GROUP BY sites.site_id
ORDER BY clients.client_id;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, sum(billing.amount) as Total_revenue, monthname(charged_datetime) as month_charge, year(charged_datetime) as year_charge
FROM clients
LEFT JOIN billing
ON clients.client_id = billing.client_id
GROUP BY clients.client_id, month_charge, year_charge
ORDER BY clients.client_id;


-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, group_concat(sites.domain_name separator ' / ') as sites
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
GROUP BY clients.client_id;