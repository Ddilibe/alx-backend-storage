-- Script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed
CREATE TRIGGER email_change
BEFORE UPDATE ON users
FOR EACH ROW 
SET NEW.valid_email = IF (OLD.email != NEW.email, 0, NEW.valid_email);
