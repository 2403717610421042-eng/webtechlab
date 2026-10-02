package com.college_event.web;

import javax.servlet.annotation.WebListener;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;

@WebListener
public class ActiveUsersListener implements HttpSessionListener {
    private static int activeSessions = 0;

    public void sessionCreated(HttpSessionEvent se) {
        activeSessions++;
        se.getSession().getServletContext().setAttribute("activeUsers", activeSessions);
    }

    public void sessionDestroyed(HttpSessionEvent se) {
        if(activeSessions > 0) activeSessions--;
        se.getSession().getServletContext().setAttribute("activeUsers", activeSessions);
    }
}
