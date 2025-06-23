-- Users
INSERT INTO users (username, token_hash, token_expires_at, token_issued_at, token_last_used_at) VALUES
('alice', 'hash_alice', '2025-07-01T12:00:00Z', '2025-06-01T12:00:00Z', '2025-06-15T12:00:00Z'),
('bob', 'hash_bob', '2025-07-15T12:00:00Z', '2025-06-10T12:00:00Z', NULL),
('charlie', NULL, NULL, NULL, NULL);

-- Task Templates
INSERT INTO task_templates (title, description, interval_frequency, interval, days_of_week, start_date, end_date, last_generated_at) VALUES
('Take out trash', 'Weekly trash removal', 'weekly', 1, 'Monday', '2025-01-01', NULL, '2025-06-20T08:00:00Z'),
('Water plants', 'Water indoor plants', 'daily', 2, NULL, '2025-01-01', NULL, '2025-06-21T07:00:00Z'),
('Pay bills', 'Monthly bill payments', 'monthly', 1, NULL, '2025-01-01', '2025-12-31', '2025-06-01T12:00:00Z');

-- Tasks
INSERT INTO tasks (template_id, title, description, display_on, due_date, completed) VALUES
(1, 'Take out trash', 'Put bins on curb', '2025-06-22', '2025-06-22', 0),
(2, 'Water plants', 'Use filtered water', '2025-06-22', '2025-06-22', 1),
(NULL, 'Ad-hoc cleanup', 'Clean garage', '2025-06-23', '2025-06-24', 0);

-- Grocery Items
INSERT INTO grocery_items (item_name, quantity, purchased) VALUES
('Milk', 2, 0),
('Bread', 1, 1),
('Eggs', 12, 0);

-- Calendar Events
INSERT INTO calendar_events (id, title, start_time, end_time, location, description) VALUES
('event1', 'Doctor Appointment', '2025-06-24T10:00:00Z', '2025-06-24T11:00:00Z', 'Clinic A', 'Annual check-up'),
('event2', 'Team Meeting', '2025-06-25T14:00:00Z', '2025-06-25T15:30:00Z', 'Online', 'Monthly planning session'),
('event3', 'Birthday Party', '2025-06-26T17:00:00Z', '2025-06-26T20:00:00Z', 'Central Park', NULL);
