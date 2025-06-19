"use client"

import { useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { ChevronLeft, ChevronRight, RotateCcw, Plus, BookOpen } from "lucide-react"

interface Flashcard {
  id: number
  front: string
  back: string
}

export default function FlashcardApp() {
  const [flashcards, setFlashcards] = useState<Flashcard[]>([
    { id: 1, front: "What is the capital of France?", back: "Paris" },
    { id: 2, front: "What is 2 + 2?", back: "4" },
    { id: 3, front: "Who wrote Romeo and Juliet?", back: "William Shakespeare" },
    { id: 4, front: "What is the largest planet in our solar system?", back: "Jupiter" },
  ])

  const [currentIndex, setCurrentIndex] = useState(0)
  const [isFlipped, setIsFlipped] = useState(false)
  const [newFront, setNewFront] = useState("")
  const [newBack, setNewBack] = useState("")
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const currentCard = flashcards[currentIndex]

  const nextCard = () => {
    setCurrentIndex((prev) => (prev + 1) % flashcards.length)
    setIsFlipped(false)
  }

  const prevCard = () => {
    setCurrentIndex((prev) => (prev - 1 + flashcards.length) % flashcards.length)
    setIsFlipped(false)
  }

  const flipCard = () => {
    setIsFlipped(!isFlipped)
  }

  const addCard = () => {
    if (newFront.trim() && newBack.trim()) {
      const newCard: Flashcard = {
        id: Math.max(...flashcards.map((c) => c.id)) + 1,
        front: newFront.trim(),
        back: newBack.trim(),
      }
      setFlashcards([...flashcards, newCard])
      setNewFront("")
      setNewBack("")
      setIsDialogOpen(false)
    }
  }

  const resetProgress = () => {
    setCurrentIndex(0)
    setIsFlipped(false)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <BookOpen className="h-8 w-8 text-indigo-600" />
            <h1 className="text-3xl font-bold text-gray-800">Flashcard Study App</h1>
          </div>
          <p className="text-gray-600">Click the card to reveal the answer</p>
        </div>

        {/* Progress Bar */}
        <div className="mb-6">
          <div className="flex justify-between items-center mb-2">
            <span className="text-sm text-gray-600">Progress</span>
            <span className="text-sm text-gray-600">
              {currentIndex + 1} of {flashcards.length}
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-indigo-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / flashcards.length) * 100}%` }}
            />
          </div>
        </div>

        {/* Flashcard */}
        <div className="mb-8">
          <Card className="h-64 cursor-pointer transition-all duration-300 hover:shadow-lg" onClick={flipCard}>
            <CardContent className="h-full flex items-center justify-center p-8">
              <div className="text-center">
                <div className="text-lg font-medium text-gray-800 mb-4">
                  {isFlipped ? currentCard?.back : currentCard?.front}
                </div>
                <div className="text-sm text-gray-500">
                  {isFlipped ? "Answer" : "Question"} • Click to {isFlipped ? "hide" : "reveal"}
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Navigation Controls */}
        <div className="flex justify-center items-center gap-4 mb-8">
          <Button
            variant="outline"
            size="lg"
            onClick={prevCard}
            disabled={flashcards.length <= 1}
            className="flex items-center gap-2"
          >
            <ChevronLeft className="h-4 w-4" />
            Previous
          </Button>

          <Button variant="outline" size="lg" onClick={flipCard} className="flex items-center gap-2">
            <RotateCcw className="h-4 w-4" />
            Flip Card
          </Button>

          <Button
            variant="outline"
            size="lg"
            onClick={nextCard}
            disabled={flashcards.length <= 1}
            className="flex items-center gap-2"
          >
            Next
            <ChevronRight className="h-4 w-4" />
          </Button>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-center gap-4">
          <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
            <DialogTrigger asChild>
              <Button className="flex items-center gap-2">
                <Plus className="h-4 w-4" />
                Add Card
              </Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Add New Flashcard</DialogTitle>
              </DialogHeader>
              <div className="space-y-4">
                <div>
                  <label className="text-sm font-medium text-gray-700 mb-2 block">Question (Front)</label>
                  <Textarea
                    placeholder="Enter the question..."
                    value={newFront}
                    onChange={(e) => setNewFront(e.target.value)}
                    className="min-h-[80px]"
                  />
                </div>
                <div>
                  <label className="text-sm font-medium text-gray-700 mb-2 block">Answer (Back)</label>
                  <Textarea
                    placeholder="Enter the answer..."
                    value={newBack}
                    onChange={(e) => setNewBack(e.target.value)}
                    className="min-h-[80px]"
                  />
                </div>
                <div className="flex justify-end gap-2">
                  <Button variant="outline" onClick={() => setIsDialogOpen(false)}>
                    Cancel
                  </Button>
                  <Button onClick={addCard} disabled={!newFront.trim() || !newBack.trim()}>
                    Add Card
                  </Button>
                </div>
              </div>
            </DialogContent>
          </Dialog>

          <Button variant="outline" onClick={resetProgress}>
            <RotateCcw className="h-4 w-4 mr-2" />
            Reset Progress
          </Button>
        </div>

        {/* Stats */}
        <div className="mt-8 text-center text-sm text-gray-600">
          <p>Total Cards: {flashcards.length}</p>
        </div>
      </div>
    </div>
  )
}
