import React from 'react'

const Expenses = ({ expenses }) => {
    return (
        <div>
        <center><h1>Average Daily Expenses</h1></center>
        {
            expenses.map((expense) => (
                <div class="expense">
                    <div class="expense_body">
                    <h5 class="expense_username">{expense.username}</h5>
                    <h5 class="expense_average">{expense.average}</h5>
                    <p class="expense_text">{"This is a text"}</p>
                    </div>
                </div>
            ))
        }
        </div>
    )
};

export default Expenses
