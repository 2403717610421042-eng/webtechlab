<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<%@ page import="javax.xml.transform.*, javax.xml.transform.stream.*, java.io.*" %>
<%
    if (session.getAttribute("user_id") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    
    int userId = (Integer) session.getAttribute("user_id");
    int totalEvents = 0;
    int registeredEvents = 0;
    int totalOrders = 0;
    
    try (Connection conn = DBConnection.getConnection()) {
        // Get total events
        PreparedStatement pst1 = conn.prepareStatement("SELECT COUNT(*) FROM events");
        ResultSet rs1 = pst1.executeQuery();
        if (rs1.next()) totalEvents = rs1.getInt(1);
        
        // Get user's registered events
        PreparedStatement pst2 = conn.prepareStatement("SELECT COUNT(*) FROM event_registrations WHERE user_id = ?");
        pst2.setInt(1, userId);
        ResultSet rs2 = pst2.executeQuery();
        if (rs2.next()) registeredEvents = rs2.getInt(1);
        
        // Get user's orders
        PreparedStatement pst3 = conn.prepareStatement("SELECT COUNT(*) FROM orders WHERE user_id = ?");
        pst3.setInt(1, userId);
        ResultSet rs3 = pst3.executeQuery();
        if (rs3.next()) totalOrders = rs3.getInt(1);
    } catch (Exception e) {
        e.printStackTrace();
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - EventSystem</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            padding: 2rem 4rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .stat-card {
            text-align: center;
            padding: 2rem;
        }
        .stat-card h3 {
            font-size: 1.2rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }
        .stat-card .stat-value {
            font-size: 3rem;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .quick-actions {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="home.jsp">Dashboard</a>
            <a href="events.jsp">Events</a>
            <a href="shop.jsp">Shop</a>
            <a href="orders.jsp">My Orders</a>
            <a href="feedback.jsp">Feedback</a>
            <a href="profile.jsp">Profile</a>
            <a href="LogoutServlet">Logout</a>
        </nav>
    </header>
    <main>
        <section class="hero" style="padding-bottom: 2rem;">
            <h1>Welcome back, <%= session.getAttribute("user_name") %>!</h1>
            <p>Your professional student portal and event dashboard.</p>
        </section>
        
        <div class="dashboard-grid">
            <div class="card stat-card">
                <h3>Available Events</h3>
                <div class="stat-value"><%= totalEvents %></div>
            </div>
            <div class="card stat-card">
                <h3>My Registrations</h3>
                <div class="stat-value"><%= registeredEvents %></div>
            </div>
            <div class="card stat-card">
                <h3>Shop Orders</h3>
                <div class="stat-value"><%= totalOrders %></div>
            </div>
        </div>
        
        <div class="quick-actions">
            <a href="events.jsp" class="btn">Explore Events</a>
            <a href="shop.jsp" class="btn" style="background: rgba(255,255,255,0.1); color: white;">Event Shop</a>
            <a href="profile.jsp" class="btn" style="background: rgba(255,255,255,0.1); color: white;">My Profile</a>
        </div>
        
        <!-- Live Database Feedback -->
        <div class="card" style="margin: 4rem auto 2rem; max-width: 1200px;">
            <h2 style="margin-bottom:1rem; color:var(--accent); text-align:center;">My Recent Feedback (Live Database)</h2>
            <div style="overflow-x:auto;">
                <table style="width: 100%; border-collapse: collapse; text-align: left;">
                    <thead>
                        <tr style="border-bottom: 2px solid var(--card-border);">
                            <th style="padding: 1rem; color: var(--accent);">Category</th>
                            <th style="padding: 1rem; color: var(--accent);">Rating</th>
                            <th style="padding: 1rem; color: var(--accent);">Message</th>
                            <th style="padding: 1rem; color: var(--accent);">Date</th>
                        </tr>
                    </thead>
                    <tbody>
                    <%
                        try (Connection connDB = DBConnection.getConnection()) {
                            PreparedStatement pstF = connDB.prepareStatement("SELECT * FROM feedback WHERE user_id = ? ORDER BY submitted_at DESC");
                            pstF.setInt(1, userId);
                            ResultSet rsF = pstF.executeQuery();
                            boolean hasFB = false;
                            while(rsF.next()) {
                                hasFB = true;
                    %>
                        <tr style="border-bottom: 1px solid var(--card-border);">
                            <td style="padding: 1rem;"><%= rsF.getString("category") %></td>
                            <td style="padding: 1rem;"><%= rsF.getInt("rating") %> / 5</td>
                            <td style="padding: 1rem;"><%= rsF.getString("message") %></td>
                            <td style="padding: 1rem;"><%= rsF.getString("submitted_at") %></td>
                        </tr>
                    <%      }
                            if (!hasFB) {
                                out.println("<tr><td colspan='4' style='padding: 1rem; text-align:center; color:var(--text-muted);'>No feedback submitted yet.</td></tr>");
                            }
                        } catch(Exception e) {}
                    %>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="card" style="margin: 4rem auto; max-width: 1200px;">
            <h2 style="margin-bottom:1rem; color:var(--accent); text-align:center;">Recent XML Feedback (Lab Requirement)</h2>
            <div style="overflow-x:auto;">
            <%
                try {
                    String xmlPath = application.getRealPath("/xml/feedback.xml");
                    String xslPath = application.getRealPath("/xml/feedback.xsl");
                    
                    if (xmlPath != null && xslPath != null) {
                        Source xmlDoc = new StreamSource(new File(xmlPath));
                        Source xslDoc = new StreamSource(new File(xslPath));
                        
                        StringWriter writer = new StringWriter();
                        Result result = new StreamResult(writer);
                        
                        TransformerFactory factory = TransformerFactory.newInstance();
                        Transformer transformer = factory.newTransformer(xslDoc);
                        transformer.transform(xmlDoc, result);
                        
                        out.println(writer.toString());
                    } else {
                        out.println("<p>Cannot resolve real path to XML/XSLT files.</p>");
                    }
                } catch (Exception e) {
                    out.println("<p style='color:red;'>Error transforming XML: " + e.getMessage() + "</p>");
                }
            %>
            </div>
        </div>
    </main>
</body>
</html>
