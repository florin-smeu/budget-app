import styled from 'styled-components';
import { BrowserRouter as Router, Link} from "react-router-dom"


/*const Wrapper = styled.section`
  padding: 4em;
  background: #dedeed;
`;*/

const Wrapper = styled.div`
  box-sizing: border-box;
  max-width: 410px;

  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;

`;

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
//padding: 1rem;
const Input = styled.input`
  border: 0px solid #999;
  margin-bottom: 1rem;
  font-size: 0.9rem;

`;

const Text = styled.h3`
  color: grey;
  align-items: center;
 `;

const SmallText = styled.pre`
  color: grey;
  font-size: 0.9rem;
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
  background: ${props => props.primary ? "white" : "white"};
  color: ${props => props.primary ? "#400e87" : "#400e87"};
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid #400e87;
  border-radius:14px;
`;


export { Button };
