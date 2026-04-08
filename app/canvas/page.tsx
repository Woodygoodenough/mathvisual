import React from 'react';
import MathGraphCanvas from '../../components/MathGraphCanvas';
import examData from '../../materials/exam_part.json';

export default function CanvasPage() {
  return (
    <main className="flex min-h-screen flex-col items-center p-10 bg-gray-50 text-gray-900 font-serif">
      <h1 className="text-3xl font-bold mb-8">Canvas Renderer</h1>
      <div className="w-full max-w-4xl gap-8 flex flex-col">
        {examData.filter(q => q.graph).map((question) => (
          <div key={question.id} className="bg-white p-6 shadow-md border rounded-lg">
             <h2 className="font-bold mb-4">Question {question.id}</h2>
             <MathGraphCanvas data={question.graph} />
          </div>
        ))}
      </div>
    </main>
  );
}
