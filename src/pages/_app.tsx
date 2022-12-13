import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      // Make the HTTP request to the Flask server
      const response = await axios.get('http://localhost:5000/api/data');

      // Update the state with the response data
      setData(response.data);
    }

    fetchData();
  }, []);

  return (
    <div>
      {data && (
        <ul>
          {Object.values(data).map(value => (
            <li>{value}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
