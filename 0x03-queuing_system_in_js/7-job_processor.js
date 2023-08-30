import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification (phoneNumber, message, job, done) {
  // Track job progress
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Track job progress
    job.progress(50, 100);

    // Log sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simulate sending a notification
    setTimeout(() => {
      // Complete the job
      done();
    }, 1000); // Simulated delay for sending the notification
  }
}

// Create a Kue queue for processing jobs
const queue = kue.createQueue({
  redis: {
    // Redis server configuration
    host: '127.0.0.1', // Change to your Redis server host if needed
    port: 6379 // Change to your Redis server port if needed
  }
});

// Process jobs from the 'push_notification_code_2' queue with a concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  // Get job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');
