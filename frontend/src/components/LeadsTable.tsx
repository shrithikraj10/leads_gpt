// src/components/LeadsTable.tsx

'use client';

import { useEffect, useState } from 'react';

export default function LeadsTable({ refresh }: { refresh: boolean }) {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    const fetchLeads = async () => {
      const res = await fetch('http://localhost:8000/leads/');
      const data = await res.json();
      setLeads(data);
    };
    fetchLeads();
  }, [refresh]);

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold mb-4">All Leads</h2>
      <table className="min-w-full border border-gray-300 text-sm">
        <thead>
          <tr className="bg-red">
            <th className="border px-4 py-2">Name</th>
            <th className="border px-4 py-2">Email</th>
            <th className="border px-4 py-2">Industry</th>
            <th className="border px-4 py-2">Created At</th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead: any) => (
            <tr key={lead.id}>
              <td className="border px-4 py-2">{lead.name}</td>
              <td className="border px-4 py-2">{lead.email}</td>
              <td className="border px-4 py-2">{lead.industry}</td>
              <td className="border px-4 py-2">{new Date(lead.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
