import React, { Component } from 'react'
import axios from 'axios'

class User extends Component {
    url = "http://localhost:8888/sign_up?username=gigel&password_hash=123"

    constructor () {
        super()
        this.state = {
            username: 'boss',
            token: '1',
        }

        this.handleClick = this.handleClick.bind(this)
    }

    handleClick () {
        axios.get(this.url)
            .then(response => this.setState({username: response.data.username}))
    }

    render() {
        return (
            <div className = 'buttonContainer'>
                <button className = 'button' onClick = {this.handleClick}>sign up</button>
                <p>Sign up successfull, {this.state.username}!</p>
                <p>Token: {this.state.token}</p>
            </div>
        )
    }

}

export default User
