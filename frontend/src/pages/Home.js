import React, { Component } from "react";
import logoImg from "../img/logo.png";
import { Card, Logo, Form, Input, Button, StyledLink, Text } from '../components/AuthForms';

class Home extends Component {
    constructor() {
        super()
    }

    render() {
        return (
            <Card>
              <Logo src={logoImg} />
              <Text> Welcome to your personal financial assistant</Text>
              <Form>

                <Button>Sign In</Button>
              </Form>
              <StyledLink to="/signup">Don't have an account?</StyledLink>
            </Card>


            /*<Card>

            <Logo src={logoImg} />
            <Text> Welcome to your personal financial assistant</Text>
            <Button>Sign In</Button>
            <StyledLink to="/signup">Don't have an account?</StyledLink>
            </Card>*/
        );
    }
}

export default Home
