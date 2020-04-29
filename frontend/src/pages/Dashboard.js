import React, { Component } from "react";
//import { Link } from 'react-router-dom';
//import logoImg from "../img/logo.png";
//import styled from 'styled-components'
import axios from 'axios'

/*

import {Button} from '../components/DashboardForms';


const Wrapper = styled.div`
    padding: 1em;
    content: "";
    display: table;
    clear: both;
    width: 80%;
`
const LeftColumnWrapper = styled.div`
    padding: 1em;
    float: left;
    background: lightgrey;
    width: 40%;
`

const RightColumnWrapper = styled.div`
    padding: 1em;
    float: right;
    background: lightgrey;
    width: 40%;
`


const Paragraph = styled.p`
    color: black;
    font-size: 0.8rem;
`
//color:grey;
const ExpensesTitle = styled.h3`
    color: papayawhip;
`

const IncomesTitle = styled.h3`
    color: lightgreen;
`
*/
class Dashboard extends Component {
    expensesUrl = "http://localhost:8888/daily_detailed_expenses?username=fsmeu"
    incomesUrl = "http://localhost:8888/daily_detailed_incomes"

    constructor() {
        super()
        this.state = {
            username: 'fsmeu',
            token: '1',
            expenses: {1: 234, 2: 3123},
            //incomes: {},
            average_daily_expenses: 0,
            average_daily_incomes: 0,
        }

        this.getExpenses = this.getExpenses.bind(this)
    }

    getExpenses() {
        axios.get(this.expensesUrl)
            .then(response => this.setState({expenses: response.data.records}))
        console.log(this.state.expenses)
    }


    render() {
        return (
            /*
          <Wrapper>
          <LeftColumnWrapper>
            <ExpensesTitle>Expenses</ExpensesTitle>
            <Button onClick = {this.getExpenses}>get expenses</Button>
            //<Paragraph> {this.getExpenses} </Paragraph>
            <Paragraph> This is my Paragraph {this.state.expenses}</Paragraph>
            <Paragraph> This is another Paragraph</Paragraph>
          </LeftColumnWrapper>
          <RightColumnWrapper>
            <IncomesTitle color="green">Incomes</IncomesTitle>
            <Paragraph> This is my Paragraph</Paragraph>
            <Paragraph> This is another Paragraph</Paragraph>
          </RightColumnWrapper>
          </Wrapper>
          */
          <div className = 'buttonContainer'>
              <button className = 'button' onClick = {this.getExpenses}>get expenses</button>
              <p>Sign up successfull, {this.state.username}!</p>

              <div>
              {
                  Object.keys(this.state.expenses).map((key, index) => (
                      <p key={index}> this is my key {key} and this is my value {this.state.expenses[key]}</p>
                  ))
              }
              </div>
          </div>

        );
    }
}

export default Dashboard;
