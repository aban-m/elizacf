## ElizaCF
A Telegram bot that selects random [CodeForces](https://www.codeforces.com) problems from a query.

#### Deployment
The bot can be hosted in, e.g., [PythonAnywhere](https://pythonanywhere.com) with webhooks, see https://github.com/aban-m/BotsAnywhere.
An instance of the bot is currently hosted at [@elizacfbot](https://t.me/elizacfbot).

#### Usage
A query string is made up of a sequence of conditions. Examples:

| Query                           | Meaning                                               |
| ------------------------------- | ----------------------------------------------------- |
| `Div2 B`                        | B problem from a Div2 contest                         |
| `rating > 1000 solvers > 30000` | Rating at most 1000 **and** solved by at least 30,000 |
| `B C +dp +math`                       | Either a B or C problem, **and**  tagged `dp` **and** `math`                  |
| `Div3 Div4 -implementation`     | Either Div3 or Div4, not tagged `implementation`      |
| `+dfs_and_similar`              | Problems tagged `dfs and similar`                     |

### Data source
The data has been pulled from the [CodeForces API](https://codeforces.com/apiHelp), saved to [static](https://github.com/aban-m/elizacf/tree/master/static).
Two post-processing steps have been applied to the resulting data:
- The `div` of each contest has been parsed (unreliably!) and added as a field to the Problem object.
- The `solvedCount` field has been copied from the "statistics" object provided by the API.
These two steps, together, lead to more query options and better performance.
