import React, { Component } from "react";
import logoImg from "../img/logo.png";
import axios from 'axios'
import { Card, Logo, Form, Input, Button, StyledLink, Text, SmallText } from '../components/AuthForms';

class Login extends Component {

    signinUrl = "http://34.70.186.236:8886/signin?email=fsmeu@gmail.com&password_hash=41e2cbe589cb11ecdc9c82feb0710ff119fe36c018ab2bd0e93a7009f478a99c"

    constructor() {
        super()
        this.state = {
            token: '1'
        }
        this.clickSignin = this.clickSignin.bind(this)
    }

    clickSignin() {
        axios.post(this.signinUrl)
            .then(response => this.setState({token: response.data.token}))
    }


    render() {
      return (
        <Card>
          <Logo src={logoImg} />
          <Form>
          <Text>Enter Account</Text>
          <SmallText>email</SmallText>
          <Input type="email" placeholder="" />
          <SmallText>password</SmallText>
          <Input type="password" placeholder="" />
          <Button onClick =  {this.clickSignin}>Sign In</Button>
          </Form>
          <StyledLink to="/signup">Don't have an account?</StyledLink>
          <div>
          <p> The token is: {this.state.token}</p>
          </div>
        </Card>
      );
    }
}


export default Login;
