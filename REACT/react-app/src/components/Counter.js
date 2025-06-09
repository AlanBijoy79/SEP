import { useState } from "react";

function Counter() {
    const [count ,setCount] = useState(0);
    function decrement() {
        setCount(count - 1);

    }
    function increment() {
        setCount(count + 1);
    }
    return (
        <div>
            <h1>Counter App</h1><hr></hr>
            <h3>{count}</h3>
            <button onClick={decrement}className="decrement">Decrement</button>
            <button onClick={increment}className="increment">Increment</button>

            </div>
    );
}
export default Counter;
