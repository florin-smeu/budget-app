import styled from 'styled-components';
import { BrowserRouter as Router, Link} from "react-router-dom"


const Wrapper = styled.section`
  padding: 4em;
  background: #dedeed;
`;

const Card = styled.div`
  box-sizing: border-box;
  max-width: 410px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  flex-direction: column;
  align-items: left;

`;

const SmallText = styled.p`
    color:grey;
    border: 0px solid #999;
    font-size: 0.9rem;
`;
//padding: 1rem;

//margin-bottom: 1rem;

const Form = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
`;

const StyledLink = styled(Link)`
  text-decoration: none;

  &:hover {
        text-decoration: none;
        color: #373762
  }
  &:focus, &:visited, &:link, &:active {
        text-decoration: none;
  }
  color: #9d9dc8;
  font-weight: bold;
`;


//400e87
const Input = styled.input`
padding: 0.5rem;
  margin-bottom: 0.2rem;
  font-size: 0.9rem;

  border: 1.5px solid grey;
  border-radius:20px;

`;

//margin: 1em;
//border: 0px solid #999;
//padding: 0.25em 1em;

const Text = styled.h3`
  color: grey;
  align-items: center;
 `;


const Logo = styled.img`
  width: 50%;
  margin-bottom: 1rem;
`;

const Error = styled.div`
  background-color: red;
`;

const ListEntry = styled.li`
  list-style-type: none;
  margin-top: 0.2em;
  margin-left: 2em;
`;



const Button = styled.button`
  /* Adapt the colors based on primary prop */
  color: ${props => props.primary ? "white" : "white"};
  background: ${props => props.primary ? "#400e87" : "#400e87"};\
  width:10em;

  font-size: 1em;
  margin-top: 3em;
  margin-bottom: 1em;
  padding: 0.25em 1em;
  border: 2px solid #400e87;
  border-radius:20px;

`;


export { Form, Input, Button, Logo, Card, Error, Wrapper, StyledLink, ListEntry, Text, SmallText };
