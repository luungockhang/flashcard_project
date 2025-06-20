class FlashcardApp {
  constructor() {
    this.flashcards = {}
    this.currentIndex = 0
    this.isFlipped = false

    this.init()
  }

  async init() {
    await this.loadCards()
    this.bindEvents()
    this.updateDisplay()
  }

  async loadCards() {
    try {
      const response = await fetch("/api/cards")
      this.flashcards = await response.json()
    } catch (error) {
      console.error("Error loading cards:", error)
    }
  }

  bindEvents() {
    // Navigation buttons
    document.getElementById("prev-btn").addEventListener("click", () => this.prevCard())
    document.getElementById("next-btn").addEventListener("click", () => this.nextCard())
    document.getElementById("flip-btn").addEventListener("click", () => this.flipCard())

    // Card click to flip
    document.getElementById("flashcard").addEventListener("click", () => this.flipCard())

    // Reset button
    document.getElementById("reset-btn").addEventListener("click", () => this.resetProgress())

    // Add card modal
    document.getElementById("add-card-btn").addEventListener("click", () => this.showAddCardModal())
    document.getElementById("cancel-btn").addEventListener("click", () => this.hideAddCardModal())
    document.getElementById("add-card-form").addEventListener("submit", (e) => this.handleAddCard(e))

    // Close modal on background click
    document.getElementById("add-card-modal").addEventListener("click", (e) => {
      if (e.target.id === "add-card-modal") {
        this.hideAddCardModal()
      }
    })
  }

  updateDisplay() {
    if (this.flashcards.length === 0) {
      document.getElementById("card-content").textContent = "No cards available"
      document.getElementById("card-type").textContent = "Add some cards to get started"
      return
    }

    const currentCard = this.flashcards[this.currentIndex]
    const content = this.isFlipped ? currentCard.back : currentCard.front
    const type = this.isFlipped ? "Answer • Click to hide" : "Question • Click to reveal"

    document.getElementById("card-content").textContent = content
    document.getElementById("card-type").textContent = type

    // Update progress
    const progressPercent = ((this.currentIndex + 1) / this.flashcards.length) * 100
    document.getElementById("progress-bar").style.width = `${progressPercent}%`
    document.getElementById("progress-text").textContent = `${this.currentIndex + 1} of ${this.flashcards.length}`
    document.getElementById("total-cards").textContent = this.flashcards.length

    // Update button states
    const hasCards = this.flashcards.length > 1
    document.getElementById("prev-btn").disabled = !hasCards
    document.getElementById("next-btn").disabled = !hasCards
  }

  // Animation
  nextCard() {
    if (this.flashcards.length > 1) {
      this.currentIndex = (this.currentIndex + 1) % this.flashcards.length
      this.isFlipped = false
      this.updateDisplay()
    }
  }

  prevCard() {
    if (this.flashcards.length > 1) {
      this.currentIndex = (this.currentIndex - 1 + this.flashcards.length) % this.flashcards.length
      this.isFlipped = false
      this.updateDisplay()
    }
  }

  flipCard() {
    if (this.flashcards.length > 0) {
      this.isFlipped = !this.isFlipped
      this.updateDisplay()
    }
  }

  resetProgress() {
    this.currentIndex = 0
    this.isFlipped = false
    this.updateDisplay()
  }

  showAddCardModal() {
    document.getElementById("add-card-modal").classList.remove("hidden")
  }

  hideAddCardModal() {
    document.getElementById("add-card-modal").classList.add("hidden")
    document.getElementById("card-front").value = ""
    document.getElementById("card-back").value = ""
  }

  async handleAddCard(e) {
    e.preventDefault()

    const front = document.getElementById("card-front").value.trim()
    const back = document.getElementById("card-back").value.trim()

    if (!front || !back) {
      alert("Please fill in both question and answer")
      return
    }

    try {
      const response = await fetch("/api/cards", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ front, back }),
      })

      if (response.ok) {
        const newCard = await response.json()
        this.flashcards.push(newCard)
        this.hideAddCardModal()
        this.updateDisplay()
      } else {
        alert("Error adding card")
      }
    } catch (error) {
      console.error("Error adding card:", error)
      alert("Error adding card")
    }
  }
}

// Initialize the app when the page loads
document.addEventListener("DOMContentLoaded", () => {
  new FlashcardApp()
})
