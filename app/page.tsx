import React from 'react';
import Link from 'next/link';

export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gray-50 text-gray-900">
        <h1 className="text-4xl font-bold mb-8">Select Renderer</h1>
        <div className="flex gap-4">
            <Link href="/svg" className="px-6 py-3 bg-blue-600 text-white rounded shadow hover:bg-blue-700">View SVG Renderer</Link>
            <Link href="/canvas" className="px-6 py-3 bg-green-600 text-white rounded shadow hover:bg-green-700">View Canvas Renderer</Link>
        </div>
    </main>
  );
}
