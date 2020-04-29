import React from "react";
import { Link } from 'react-router-dom';
import logoImg from "../img/logo.png";
import { Card, Logo, Form, Input, Button, StyledLink, Wrapper, Text, SmallText } from '../components/AuthForms';

function Signup() {
  return (
    <Card>
      <Logo src={logoImg} />
      <Form>
        <Text>Create Account</Text>
        <SmallText>email</SmallText>
        <Input type="email" placeholder="" />
        <SmallText>password</SmallText>
        <Input type="password" placeholder="" />
        <SmallText>confirm password</SmallText>
        <Input type="password" placeholder="" />
        <Button>Sign Up</Button>
      </Form>
      <StyledLink to="/login">Already have an account?</StyledLink>
    </Card>
  );
}

export default Signup;
