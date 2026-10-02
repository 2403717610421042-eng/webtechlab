<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<%
    try (Connection conn = DBConnection.getConnection()) {
        conn.createStatement().execute("INSERT INTO events (event_name, event_date, venue, max_members, registered_members) VALUES ('AI & Machine Learning Workshop', '2026-11-25 14:00:00', 'Seminar Hall 3', 150, 0)");
        conn.createStatement().execute("INSERT INTO events (event_name, event_date, venue, max_members, registered_members) VALUES ('Annual Music Fest', '2026-12-10 18:00:00', 'Main Ground', 2000, 0)");
        conn.createStatement().execute("INSERT INTO events (event_name, event_date, venue, max_members, registered_members) VALUES ('Hackathon 2026', '2026-12-15 08:00:00', 'CS Building', 300, 0)");
        
        conn.createStatement().execute("INSERT INTO products (name, description, price, image_url) VALUES ('Official Event Cap', 'Premium embroidered college cap', 12.50, 'cap.png')");
        conn.createStatement().execute("INSERT INTO products (name, description, price, image_url) VALUES ('Tech Sticker Pack', '5 cool laptop stickers', 4.99, 'stickers.png')");
        conn.createStatement().execute("INSERT INTO products (name, description, price, image_url) VALUES ('Event Notebook', 'Ruled notebook with event branding', 8.00, 'notebook.png')");
        conn.createStatement().execute("INSERT INTO products (name, description, price, image_url) VALUES ('Coffee Mug', 'Ceramic college mug', 14.00, 'mug.png')");
        
        out.println("SUCCESS");
    } catch (Exception e) {
        out.println("ERROR: " + e.getMessage());
    }
%>
