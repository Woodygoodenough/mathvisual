import React from 'react';
import MathGraph from '../components/MathGraph';
import examData from '../materials/exam_part.json';
import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';

// Basic regex to replace LaTeX delimiters with Katex components
const renderTextWithMath = (text: string) => {
  const parts = text.split(/(\$.*?\$)/g);
  return parts.map((part: string, index: number) => {
    if (part.startsWith('$') && part.endsWith('$')) {
      const mathStr = part.substring(1, part.length - 1);
      return <InlineMath key={index} math={mathStr} />;
    }
    return <span key={index}>{part}</span>;
  });
};

export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-gray-50 text-gray-900 font-serif">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex flex-col gap-12">
        <h1 className="text-4xl font-bold mb-8">Math Exam Viewer</h1>

        {examData.map((question) => (
          <div key={question.id} className="bg-white p-8 rounded-xl shadow-md w-full mb-8">
            <div className="flex gap-4 mb-6">
              <span className="font-bold text-xl">{question.id}.</span>
              <p className="text-lg leading-relaxed">
                {renderTextWithMath(question.text)}
              </p>
            </div>

            {question.graph && (
              <div className="flex justify-center w-full mb-8">
                <MathGraph data={question.graph} />
              </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 ml-8">
              {Object.entries(question.choices || {}).map(([key, choice]) => (
                <div
                  key={key}
                  className={`flex items-center gap-3 p-3 rounded-lg border ${question.answer === key ? 'border-green-500 bg-green-50' : 'border-gray-200'}`}
                >
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center font-bold ${question.answer === key ? 'bg-green-500 text-white' : 'bg-gray-100'}`}>
                    {key}
                  </div>
                  <div className="text-lg">
                    {renderTextWithMath(choice)}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
