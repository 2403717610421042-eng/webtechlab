<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<%
    try (Connection conn = DBConnection.getConnection()) {
        String sql = "CREATE TABLE IF NOT EXISTS feedback (" +
                     "id INT AUTO_INCREMENT PRIMARY KEY," +
                     "user_id INT NOT NULL," +
                     "category VARCHAR(100)," +
                     "rating INT," +
                     "message TEXT NOT NULL," +
                     "submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP," +
                     "FOREIGN KEY (user_id) REFERENCES users(id))";
        conn.createStatement().execute(sql);
        out.println("SUCCESS");
    } catch (Exception e) {
        out.println("ERROR: " + e.getMessage());
    }
%>
