// src/app/page.tsx

'use client';

import { useState } from 'react';
import CreateLeadForm from '../components/CreateLeadForm';
import LeadsTable from '../components/LeadsTable';

export default function HomePage() {
  const [refreshToggle, setRefreshToggle] = useState(false);

  const handleLeadCreated = () => {
    setRefreshToggle((prev) => !prev);
  };

  return (
    <main className="max-w-2xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">LeadsGPT MVP</h1>
      <CreateLeadForm onLeadCreated={handleLeadCreated} />
      <LeadsTable refresh={refreshToggle} />
    </main>
  );
}
