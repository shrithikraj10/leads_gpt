// src/components/CreateLeadForm.tsx

'use client';

import { useState } from 'react';

export default function CreateLeadForm({ onLeadCreated }: { onLeadCreated: () => void }) {
  const [form, setForm] = useState({ name: '', email: '', industry: '' });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await fetch('http://localhost:8000/leads/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    });
    setForm({ name: '', email: '', industry: '' });
    onLeadCreated(); // Refresh the leads list
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="text"
        placeholder="Name"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
        className="border p-2 w-full"
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={(e) => setForm({ ...form, email: e.target.value })}
        className="border p-2 w-full"
        required
      />
      <input
        type="text"
        placeholder="Industry"
        value={form.industry}
        onChange={(e) => setForm({ ...form, industry: e.target.value })}
        className="border p-2 w-full"
        required
      />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Create Lead
      </button>
    </form>
  );
}
