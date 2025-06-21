import { useEffect, useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage('Failed to fetch backend'));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">LeadsGPT Frontend</h1>
      <p className="mt-4">{message}</p>
    </div>
  );
}
