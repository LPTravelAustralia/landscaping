// Accordion Fix - Handle clicks on accordion titles to expand/collapse content
(function() {
    function initAccordions() {
        // Find all accordion item containers
        const accordionItems = document.querySelectorAll('[data-grab="accordion-item-container"]');
        
        accordionItems.forEach(item => {
            const titleWrapper = item.querySelector('[data-grab="accordion-item-title-wrapper"]');
            const contentWrapper = item.querySelector('.dygwmn');
            
            if (titleWrapper && contentWrapper) {
                // Set initial state
                contentWrapper.style.maxHeight = '0px';
                contentWrapper.style.overflow = 'hidden';
                titleWrapper.style.cursor = 'pointer';
                
                // Add click handler to title
                titleWrapper.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    // Toggle expanded state
                    const isExpanded = contentWrapper.style.maxHeight !== '0px' && contentWrapper.style.maxHeight !== '';
                    
                    // Close all other accordion items
                    accordionItems.forEach(otherItem => {
                        if (otherItem !== item) {
                            const otherContent = otherItem.querySelector('.dygwmn');
                            const otherTitle = otherItem.querySelector('[data-grab="accordion-item-title-wrapper"]');
                            if (otherContent) {
                                otherContent.style.maxHeight = '0px';
                            }
                            if (otherTitle) {
                                otherTitle.setAttribute('aria-expanded', 'false');
                            }
                        }
                    });
                    
                    if (isExpanded) {
                        // Collapse
                        contentWrapper.style.maxHeight = '0px';
                        titleWrapper.setAttribute('aria-expanded', 'false');
                    } else {
                        // Expand - calculate the actual height of content
                        const content = contentWrapper.querySelector('[data-grab="accordion-item-desc"]');
                        if (content) {
                            const height = content.scrollHeight;
                            contentWrapper.style.maxHeight = (height + 32) + 'px'; // 32px for padding
                        } else {
                            contentWrapper.style.maxHeight = '500px'; // Fallback height
                        }
                        titleWrapper.setAttribute('aria-expanded', 'true');
                    }
                });
                
                // Also handle keyboard interaction
                titleWrapper.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        titleWrapper.click();
                    }
                });
                
                // Set initial aria-expanded state
                titleWrapper.setAttribute('aria-expanded', 'false');
            }
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAccordions);
    } else {
        initAccordions();
    }
    
    // Also initialize after a short delay for dynamically loaded content
    setTimeout(initAccordions, 500);
    setTimeout(initAccordions, 1500);
})();
