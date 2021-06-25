import queries
import generators
import logics

logics.logic_1000_reversed(
    login_generator=generators.PopPasswordGenerator(),
    password_generator=generators.PopPasswordGenerator(),
    query=queries.request_local_server
)
