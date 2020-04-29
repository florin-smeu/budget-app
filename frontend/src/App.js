import React, { Component } from 'react'
import { BrowserRouter as Router, Link, Route } from "react-router-dom"
import Home from "./pages/Home"
import Admin from "./pages/Admin"
import PrivateRoute from './PrivateRoute';
import { AuthContext } from "./context/auth";
import Login from "./pages/Login";
import Signup from './pages/Signup';
import Dashboard from "./pages/Dashboard"
import { Card, Logo, Form, Input, Button, StyledLink, ListEntry } from './components/AuthForms';

import logo from './logo.svg'
import './App.css'
import Expenses from './components/expenses'
import User from './components/user'

class App extends Component {
    /*const existingTokens = JSON.parse(localStorage.getItem("tokens"))
    const [authTokens, setAuthToken] = useState(existingTokens)

    const setTokens = (data) => {
        localStorage.setItem("tokens", JSON.stringify(data))
        setAuthToken(data)
    }*/


    render() {
        return (
            <AuthContext.Provider value={true}>
            <Router>
            <div>
                <ListEntry>
                  <StyledLink to="/">Home Page</StyledLink>
                </ListEntry>
                <ListEntry>
                  <StyledLink to="/admin">Admin Page</StyledLink>
                </ListEntry>
                <ListEntry>
                  <StyledLink to="/dashboard">Dashboard</StyledLink>
                </ListEntry>
              <Route exact path="/" component={Home} />
              <Route path="/login" component={Login} />
              <Route path="/signup" component={Signup} />
              <PrivateRoute path="/admin" component={Admin} />
              <PrivateRoute path="/dashboard" component={Dashboard} />
            </div>
            </Router>
            </AuthContext.Provider>
        )
    }
}


export default App
