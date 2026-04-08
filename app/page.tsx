import React from 'react';
import MathGraphSVG from '../components/MathGraphSVG';
import examData from '../materials/exam_part.json';

export default function Page() {
  const complexQs = [26, 29, 30, 34, 35];

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12 bg-gray-50 text-gray-900 font-serif">
      <div className="z-10 max-w-4xl w-full items-center justify-between font-mono text-sm lg:flex flex-col gap-12">
        <h1 className="text-4xl font-bold mb-8">Simplified Graph Viewer</h1>

        {examData.filter(q => complexQs.includes(q.id)).map((question) => (
          <div key={question.id} className="bg-white p-8 rounded-xl shadow-md w-full mb-8">
            <div className="flex gap-4 mb-6">
              <span className="font-bold text-xl">{question.id}.</span>
              <p className="text-lg leading-relaxed whitespace-pre-wrap">
                {question.text}
              </p>
            </div>

            {question.graph && (
              <div className="flex justify-center w-full mb-8">
                <MathGraphSVG data={question.graph} />
              </div>
            )}
          </div>
        ))}
      </div>
    </main>
  );
}
